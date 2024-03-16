# Blogging Platform API with Django and Django Rest Framework

This project is a RESTful API for a blogging platform built using Django and Django Rest Framework. The API includes user authentication and authorization, allowing users to register, log in, and perform actions like creating, reading, updating, and deleting blog posts.

## ER diagram
# link -> https://dbdiagram.io/d/Blog-ER-diagram-65af9780ac844320ae86219c
![](https://github.com/Benji918/DRF_blog/blob/master/Blog%20ER%20diagram%20(1).png)  

## Architectural Diagram
![](https://github.com/Benji918/DRF_blog/blob/master/Blank%20diagram.jpeg)   


## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Authorization](#authorization)
- [Docker](#docker)


## Features

1. **User Authentication and Authorization:**
   - User Registration
   - User login with JWT authentication
   - Authorization to ensure only authenticated users can perform certain actions.

2. **Blog Post Management:**
   - Create a new blog post
   - Read existing blog posts
   - Update an existing blog post
   - Delete an existing blog post

3. **Blog Post Attributes:**
   - Each blog post has a title, content, author, and timestamp.

## Technologies

- Django
- Django Rest Framework


## Getting Started

### Prerequisites

- Python
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DRF_blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DRF_blog
   ```

3. Create a `.env` file in the project root and configure your environment variables:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   ```

   Replace `your_secret_key` with a secure random key.

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run project:
   ```bash
   py manage.py runserver
   ```

5. Access the API at [https://drfblog-production.up.railway.app/api/schema/swagger/#/blog/blog_user_update].

## Usage

The API is now accessible, and you can start interacting with it using tools like [Postman](https://www.postman.com/) or [curl](https://curl.haxx.se/). Here are some common API endpoints:

### API Endpoints

- **User Registration:**
  - Endpoint: `POST /api/auth/register/`
  - Payload: `{ "username": "your_username", "email": "your_email@example.com", "password": "your_password" }`

- **User Login:**
  - Endpoint: `POST /api/auth/login/`
  - Payload: `{ "username": "your_username", "password": "your_password" }`
  - Returns a JWT token upon successful login.

- **Create Blog Post:**
  - Endpoint: `POST /api/blog/`
  - Payload: `{ "title": "Your Blog Title", "content": "Your blog content" }`
  - Requires authentication.

- **Read Blog Posts:**
  - Endpoint: `GET /api/blog/`
  - Returns a list of all blog posts.

- **Update Blog Post:**
  - Endpoint: `PUT /api/blog/{blog_post_id}/`
  - Payload: `{ "title": "Updated Title", "content": "Updated content" }`
  - Requires authentication and ownership.

- **Delete Blog Post:**
  - Endpoint: `DELETE /api/blog/{blog_post_id}/`
  - Requires authentication and ownership.

### Authentication

Authentication is handled using JWT (JSON Web Tokens). Include the obtained token in the Authorization header for protected endpoints:

```http
Authorization: JWT your_jwt_token
```

### Authorization

Authorization is implemented to ensure that only authenticated users can perform actions like creating, updating, and deleting blog posts. The API uses a custom permission class (`IsOwnerOrReadOnly`) to determine if the requesting user is the owner of the blog post.



