import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  # Take the request's arguments to get the page number
  page = request.args.get('page', 1, type=int)
  # Set the start and end based on the 'QUESTIONS_PER_PAGE'
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  # Use the ListInterpolation to format the questions appropriately
  questions = [question.format() for question in selection]
  # Set the current page questions from start to end
  current_questions = questions[start:end]

  # Return a set of questions for the specific request
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories') # The default method is GET
  def get_categories():
    # Retrieve all categories from the database
    categories = Category.query.all()
    # Return a jsonify with the categories and set success to true
    return jsonify({
      'success': True,
      # Use the ListInterpolation to format the categories based on their ids and types
      'categories': {category.id: category.type for category in categories},
    })


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/questions')  # The default method is GET
  def get_questions():
    # Retrieve all questions from the database ordered by their IDs
    selection = Question.query.order_by(Question.id).all()
    # Call the 'paginate_questions' function to get the current page questions
    current_questions = paginate_questions(request, selection)
    # Retrieve all categories from the database
    categories = Category.query.all()

    # Check if the page number is out of range (page is not found)
    if len(current_questions) == 0:
      # Send 404 status code 
      abort(404)

    # Return a jsonify with the questions, total_questions, categories, current_cateogry and set the success body to true
    return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        # Use the ListInterpolation to format the categories based on their ids and types
        'categories': {category.id: category.type for category in categories},
        # At first the current category is not selected
        'current_category': None 
    })


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  # Set the method to DELETE and the <variable_name> to <question_id>
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      # Retrieve the specified question by its ID
      question = Question.query.get(question_id).one_or_none()

      # Check if the question exists or not
      if question is None:
        # If the question doesn't exist, send an error (resource isn't found - 404)
        abort(404)
      
      # If the question exists, delete it
      question.delete()
      
      # Return a jsonify with the question's ID and set the success body to true
      return jsonify({
          'success': True,
          'deleted': question.id, #id
      })
    except:
      # If an error occured while proccessing the DELETE, send an error (unprocessable - 422)
      abort(422)


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  # Set the method to POST
  @app.route('/questions', methods=['POST'])
  def add_question():
    # Get the body from the requesst
    body = request.get_json()

    # Check if the user filled the fields or not
    if (body.get('question') == '') or (body.get('answer') == '') or (body.get('difficulty') == '') or (body.get('category') == ''):
      # If at least one of the fields is empty, send an error (unprocessable - 422)
      abort(422)

    # Store the form data to variables
    new_question = body.get('question')
    new_answer = body.get('answer')
    new_difficulty = body.get('difficulty')
    new_category = body.get('category')

    try:
      # Create an instance of the Question model with the form data
      question = Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty)
      # Insert the new quetion to the database
      question.insert()

      # Return a jsonify with the created question's ID and set success body to true
      return jsonify({
          'success': True,
          'created': question.id,
      })
    
    except:
      # If an error occured while proccessing the INSERT, send an error (unprocessable - 422)
      abort(422)



  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  # Set the method to POST and set the route to have '/search/ so it differs from POST new question
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    # Get the body from the requesst
    body = request.get_json()
    # Get the 'searchTerm' the user entered
    search_term = body.get('searchTerm')

    if search_term is None:
      abort(404)
    
    # Retrieve all questions by using ilike function for the search term
    # (Reference: https://prodevsblog.com/questions/146983/case-insensitive-flask-sqlalchemy-query/)
    results = Question.query.filter(Question.question.ilike("%" + search_term + "%")).all()

    if results is None:
      abort(422)

    # Return a jsonify with the created question's ID and set success body to true
    return jsonify({
        'success': True,
        # Use the ListInterpolation to format the questions appropriately
        'questions': [question.format() for question in results],
        'total_questions': len(results),
        'current_category': None
    })

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  # Set the <variable_name> to <category_id> and the default method is GET
  @app.route('/categories/<int:category_id>/questions')
  def get_category_questions(category_id):
    # Retrieve the category from the database by its ID
    category = Category.query.get(category_id)

    # Check if the category exists or not (if the user writes the URL with non-existent category ID)
    if category is None:
        # If the category doesn't exist, send an error (resource isn't found - 404)
        abort(404)

    # Retrieve all the questions of the specified category from the database
    questions = Question.query.filter(Question.category == category_id).all()

    # Return a jsonify with the created question's ID and set success body to true
    return jsonify({
      'success': True,
      # Use the ListInterpolation to format the questions appropriately
      'questions': [question.format() for question in questions],
      'total_questions': len(questions),
      'current_category': category_id  # Set the specified category
    })

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  # Set the method to POST
  @app.route('/quizzes', methods=['POST'])
  def play():
    # Get the body from the requesst
    body = request.get_json()
    
    # Get the selected category
    category = body.get('quiz_category')
    # Get the previous questions
    previous_questions = body.get('previous_questions')

    # If the user chooses (ALL)
    if(category['type'] == 'click'):
      questions = Question.query.all()
    else:
      questions = Question.query.filter(Question.category == category['id']).all()
    
    new_questions = []
    for question in questions:
      # https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
      if question.id not in previous_questions:
        new_questions.append(question)

    if len(new_questions) == 0:
      next_question = None
    else:
      next_question

    # Return a jsonify with the created question's ID and set success body to true
    return jsonify({
        'success': True,
        'question': None
    })








  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    
