# FastAPI - A Python Framework Course

## Overview

FastAPI is a modern, high-performance web framework for building APIs with Python 3.10+ that leverages standard Python type hints. This course provides a step-by-step guide to mastering FastAPI, from installation to deployment, ensuring you can create robust and efficient APIs.

## Features

- **Automatic Documentation**: Generate interactive API documentation effortlessly using Swagger UI and ReDoc.
- **Asynchronous Programming**: Utilize Python's async capabilities for improved performance.
- **Data Validation**: Leverage Pydantic for data validation and serialization.
- **Database Integration**: Connect to SQL and NoSQL databases seamlessly.
- **User Authentication**: Implement secure user authentication with JWT.
- **Error Handling**: Manage exceptions and status codes effectively.

## Course Structure

1. **Framework Intro**: Introduction to FastAPI and its advantages.
2. **Course Intro**: Overview of what you will learn throughout the course.
3. **Install and Setup**: Setting up FastAPI and necessary dependencies.
4. **Break it Down**: Understanding the basic structure of a FastAPI application.
5. **Path Parameters**: Using path parameters in API endpoints.
6. **API Docs**: Exploring automatic API documentation features.
7. **Query Parameters**: Handling query parameters in requests.
8. **Request Body**: Working with request bodies for data input.
9. **Debugging**: Techniques for debugging your FastAPI applications.
10. **Pydantic Schemas**: Using Pydantic for data validation and serialization.
11. **Database Connection**: Connecting FastAPI to a database.
12. **Create Model and Tables**: Defining models and creating database tables.
13. **Store Blog to Database**: Implementing functionality to store blog posts.
14. **Get Blog from Database**: Retrieving blog posts from the database.
15. **Exception & Status Code**: Handling exceptions and returning appropriate status codes.
16. **Delete a Blog**: Implementing blog deletion functionality.
17. **Response Model**: Creating response models for structured output.
18. **Create User**: Implementing user creation functionality.
19. **Hash Password**: Securing passwords with hashing.
20. **Show User**: Displaying user information.
21. **Using Doc Tags**: Organizing API documentation with doc tags.
22. **Relationship**: Managing relationships between data models.
23. **API Router**: Structuring your application with API routers.
24. **API Router Path Operators**: Using path operators with API routers.
25. **Login & Verify Password**: Implementing user login and password verification.
26. **JWT Access Token**: Generating and using JWT access tokens for authentication.
27. **Route Behind Authentication**: Protecting routes with authentication.

## Installation

To get started with FastAPI, ensure you have Python 3.6+ installed. Follow these steps:

```bash
# Create a virtual environment
python3 -m venv fastapi-env

# Activate the virtual environment
# On Windows
source fastapi-env\Scripts\activate
# On macOS/Linux
source fastapi-env/bin/activate

# Install FastAPI and Uvicorn
pip install fastapi uvicorn

# Copy environment variables
cp .env.example .env
```

## Running the Application

Navigate to the directory containing your `main.py` file and run the following command:

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`. Access the API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

We welcome contributions to this course! If you have feedback, suggestions, or improvements, feel free to:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

## License

This course is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Acknowledgments

This course is inspired by the teachings of Bitfumes and the official [FastAPI documentation](https://fastapi.tiangolo.com/).
