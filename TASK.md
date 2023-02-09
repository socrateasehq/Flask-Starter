## Equip Assignment 

## Problem Statement
You are building a Learning Management System (LMS) where content creators can create tests. Tests have different types of questions like MCQ’s, Multiple Correct Answers. Test Takers can take these tests as many times as are allowed by the content creator. Below are the tables which have been defined

User, Test, Question, UserResponse, UserProgress. You can check out the schema of the tables in the models/__ init __.py file.
In Question model, for the question_types the sample of the content is defined in the get_sample_content method. You can use this to generate sample content for the question_types.

## Tasks

Set up the repository by following the steps in the README.md file.
Create a new branch and name it as your name.

1. Generate mock content for all the tables. Create a few tests, with a few questions in each test. Also create a few users and assign them to a classroom. 
Create a few user responses for each test. Make sure that you assign a user to a classroom, as you will need to write some APIs which will return data based on the classroom_id. You can use the faker library to generate mock data.
While generating responses to questions, MCQ's can have only a single correct answer, so assigning points here is straightforward. For MCA's, come up with a formula to calculate points based on the number of correct answers which were selected.


2.  Write an API where given a test and a user, for each question in the test, it returns the following:
- question contents, the points 
- the response of the user
- whether they got it correct or not
- the number of points they scored

Remember, some users may not have attempted all the questions in the test. In that case, you need to return the question details, with response, points, got correct answer as null

3. Given a classroom_id and a test_id, for all users in the classroom find out for each question in the test, whether they got it right or not

The result should be something like this

| Test Taker Name   | Question 1 | Question 2 | Question 3 | Question 4 | Question 5 |
|-------------------|------------|------------|------------|------------|------------|
| Random user       | correct      | wrong        | correct       | wrong         | not attempted |
| Another user      | not attempted | not attempted | not attempted | not attempted | not attempted
|  Yet another user | wrong        | correct       | wrong        | correct       | wrong|

Write an API to return the data above.
 
4. Given a test ID, for each question, find out what percentage of test takers have selected which option.

5. Given a test ID, write an API to update the questions in a test. Given a test_id, and a list of all questions in the payload, you need to update the questions in the database based on the input which is given. 
The questions can be reordered in the payload, and this must be updated in the db too. Remember, there is unique constraint on test_id, question_number  
