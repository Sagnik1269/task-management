# Task Management API - Project Tasks

## Frontend

### API Testing Tools
- [ ] Set up Postman or Swagger for testing all API endpoints.
- [ ] Create a Postman collection for API testing with examples for:
  - Authentication (`/auth/register`, `/auth/login`).
  - Task CRUD operations (`GET /tasks`, `POST /tasks`, etc.).
  - `/users/me` profile endpoint.
- [ ] Validate endpoint responses for correct status codes and data structures.

### UI Design (Optional)
- [x] Create a wireframe for a basic web UI for task management.
- [x] Implement a login page that accepts username and password.
- [ ] Build a task dashboard:
  - Display tasks in a list with filtering options for status and priority.
  - Support pagination with a "Load More" or page navigation buttons.
- [ ] Add forms for creating and updating tasks.
- [ ] Display success and error messages for API responses.

### API Documentation
- [ ] Write OpenAPI/Swagger documentation for:
  - `/auth/register` and `/auth/login` endpoints.
  - Task management endpoints (`/tasks`, `/tasks/{task_id}`).
  - `/users/me` profile endpoint.
- [ ] Host documentation locally using Swagger UI or ReDoc.

### Testing the Endpoints
- [ ] Verify JWT token authentication for protected routes using Postman.
- [ ] Test filtering and pagination for `GET /tasks` with different query parameters.
- [ ] Simulate invalid inputs to test API error handling.

---

## Backend

### Framework Setup
- [ ] Create a Flask or FastAPI project structure:
  - `app/` folder with subdirectories for `routes`, `models`, and `services`.
- [ ] Add `config.py` for environment variables (e.g., secret key, database URL).
- [ ] Set up a virtual environment and install required libraries (e.g., Flask/FastAPI, SQLAlchemy).

### Middleware
- [ ] Add JWT token middleware to protect routes.
- [ ] Configure CORS (if applicable).
- [ ] Implement rate limiting (bonus).

### Authentication Implementation
#### User Registration (`POST /auth/register`)
- [ ] Validate input fields (e.g., username, email format).
- [ ] Hash passwords securely using `bcrypt` or `argon2`.
- [ ] Save user details to the database.
- [ ] Return a JWT token upon successful registration.

#### User Login (`POST /auth/login`)
- [ ] Verify user credentials against stored data.
- [ ] Generate a JWT token with a 1-hour expiration.
- [ ] Include error handling for incorrect credentials or inactive accounts.

### Task Management Endpoints
#### List Tasks (`GET /tasks`)
- [ ] Implement query parameters for filtering by status and priority.
- [ ] Add pagination with a default of 10 items per page.
- [ ] Ensure only the authenticated user’s tasks are retrieved.

#### Create Task (`POST /tasks`)
- [ ] Validate required fields (title, status, priority).
- [ ] Associate the new task with the authenticated user.
- [ ] Add error handling for invalid or missing fields.

#### Update Task (`PUT /tasks/{task_id}`)
- [ ] Fetch the task by `task_id` and ensure it belongs to the authenticated user.
- [ ] Update task fields such as title, description, status, and priority.
- [ ] Include a timestamp for the `updated_at` field.
- [ ] Handle errors for missing or unauthorized tasks.

#### Delete Task (`DELETE /tasks/{task_id}`)
- [ ] Soft delete the task (set an `is_deleted` flag).
- [ ] Ensure only the authenticated user can delete their tasks.

### User Profile
#### Get Profile (`GET /users/me`)
- [ ] Fetch authenticated user details from the database.
- [ ] Exclude sensitive fields like password hash.
- [ ] Return profile data in a structured response.

### Database Design
- [ ] Create the `User` model with fields:
  - `username` (unique).
  - `email` (unique).
  - `password_hash`.
  - `created_at`.
- [ ] Create the `Task` model with fields:
  - `title`, `description`, `status`, `priority`.
  - `created_at`, `updated_at`.
  - Foreign key `user_id`.

### Migrations
- [ ] Set up Alembic for database migrations (if using Flask).
- [ ] Generate initial migration script for tables.
- [ ] Apply migrations to the database.

### Error Handling and Validation
#### Input Validation
- [ ] Add validation for user registration and login (e.g., valid email, strong passwords).
- [ ] Validate task inputs like title (non-empty) and status/priority (valid enums).

#### Error Handling
- [ ] Return appropriate error responses (e.g., 400 for bad requests, 401 for unauthorized).
- [ ] Log errors for debugging.

### Testing
#### Unit Tests
- [ ] Write Pytest test cases for:
  - Authentication endpoints.
  - Task CRUD operations.
  - Profile retrieval.

#### Integration Tests
- [ ] Test end-to-end workflows, such as registering a user and creating tasks.
- [ ] Validate database integrity after operations.