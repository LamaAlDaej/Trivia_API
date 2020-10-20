# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)


## Introduction

The Trivia application lets Udacity's employees and students start holding trivia and seeing who's the most knowledgeable of the bunch.
The app can do the following tasks:
1) Display questions - both all questions and by category.
2) Delete questions.
3) Add questions.
4) Search for questions.
5) Play the quiz game.

## Getting Started
### Base URL
This app can only be run locally. 
- Backend: http://127.0.0.1:5000/
- Frontend: http://127.0.0.1:3000/
### Authentication: 
This version of the Trivia application does not require authentication or API keys.

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```

### Error Types and Messages
The Trivia API will return the below error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable
- 405: Method Not Allowed
- 400: Bad Request
- 500: Internal Server Error

## Resource Endpoint Library
### GET '/categories'
* Genreal
    * Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    * Request Arguments: None
    * Returns: An object that contains an object with a single key, categories, that contains a object of id: category_string key:value pairs, and a success boolean value.
* Sample: `curl http://127.0.0.1:5000/categories`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```


### GET '/categories/<int:category_id>/questions'
* Genreal
    * Retrieves all the questions for a specific category
    * Request Arguments: Category's ID (category_id)
    * Returns: An object that contains a success boolean value, list of the specified category's questions, number of total questions, and the ID of the current category.
* Sample: `curl http://127.0.0.1:5000/categories/1/questions`
```
{
  "current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

### GET '/questions'
* Genreal
    * Retrieves all the questions and categories
    * Request Arguments: None
    * Returns: An object that contains a success boolean value, a list of the current page questions (10 questions per page), number of total questions, list of categories in key:value pairs, and the ID of the current category.
* Sample: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 26
}
```

### POST '/questions'
* General
    * Creates a new question
    * Request Arguments: None
    * Returns: An object that contains a success boolean value and the ID of the created question.
* Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is the nearest planet to the sun?","answer":"Mercury","difficulty":"1","category":"1"}'`
```
{
  "created": 36,
  "success": true
}
```

### DELETE '/questions/<int:question_id>'
* Genreal
    * Removes a question using its ID
    * Request Arguments: The question's ID (question_id)
    * Returns: An object than contains a success boolean value and the ID of the deleted question.
* Sample: `curl -X DELETE http://127.0.0.1:5000/questions/10`
```
{
  "deleted": 10,
  "success": true
}
```

### POST '/questions/search'
* General
    * Fiends questions based on a search term
    * Request Arguments: None
    * Returns: An object that contains a success boolean value, list of the result questions, number of total questions, and the ID of the current category.
* Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d "{\"searchTerm\":\"title\"}"`
```
{
  "current_category": null,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

### POST '/quizzes'
* General
    * Plays a quiz for a specific category questions or all categories' questions
    * Request Arguments: None
    * Returns: An object that contains a success boolean value and the next question to be asked.
* Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "content-type: application/json" -d "{\"quiz_category\":{\"type\":\"Science\",\"id\":1},\"previous_questions\":[]}"`
```
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
  "success": true
}
```
