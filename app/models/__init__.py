from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from enum import Enum

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True, nullable=False)
    classroom_id = db.Column(db.Integer)  # This will usually be a foreign key, but for the sake of simplicity, we'll just use an integer


class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    max_attempts = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    total_points = db.Column(db.Integer)


class QuestionTypesEnum(str, Enum):

    mcq = 'mcq'
    mca = 'mca'

    def __str__(self):
        return self.value


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(JSONB, default={})
    type = db.Enum(QuestionTypesEnum)
    question_number = db.Column(db.Integer)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    points_assigned = db.Column(db.Integer)

    __table_args__ = (UniqueConstraint('test_id', 'question_number', name='_test_question_number_uq'),)

    def generate_sample_content(self):

        if self.type.value == 'mcq':
            contents = {"question": "What is 5 + 7?", "choices": [2, 12, 2, 4], "correct_ans_index": 1}
        elif self.type.value == 'mca':
            contents = {
                "question": "Which of the following are countries", "choices": ["Madrid", "Spain", "Tokyo", "Japan"],
                "correct_ans_indices": [1, 2]
                }
        else:
            raise ValueError("Invalid question type")

        return contents


# When a user starts a test, a record should be created in the user_progress table, and when the user finishes the test,
# the record should be updated with the finished_at, is_finished fields, total_points_scored and percentage_scored
# fields


class UserProgress(db.Model):
    __tablename__ = 'user_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime)
    is_finished = db.Column(db.Boolean, default=False)
    total_points_scored = db.Column(db.Integer, default=0)
    percentage_scored = db.Column(db.Integer, default=0)


class UserResponse(db.Model):
    __tablename__ = 'user_responses'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    response = db.Column(JSONB, default={})
    is_correct = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    up_id = db.Column(db.Integer, db.ForeignKey('user_progress.id'))
    points_scored = db.Column(db.Integer)