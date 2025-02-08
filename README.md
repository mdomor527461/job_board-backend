# Job Board API Documentation

## Base URL

```
https://your-domain.com/api/](http://job-board-backend-lemon.vercel.app
```

---

## Authentication

- **Login** and **Register** endpoints are available for user authentication.
- Token-based authentication is used for secured endpoints.

---

## User APIs

### Register a New User

**POST** `/api/users/register/`

**Request Body:**
```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "image": "file (optional)"
}
```

**Response:**
```json
{
  "id": "integer",
  "username": "string",
  "email": "string",
  "image_url": "string"
}
```

---

### User Login

**POST** `/api/users/login/`

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "token": "string",
  "user_id": "integer",
  "user_type": "string",
  "image_url": "string",
  "is_premium": "boolean"
}
```

---

### User Logout

**POST** `/api/users/logout/`

**Headers:**
```
Authorization: Token <your_token>
```

**Response:**
```json
{
  "detail": "Logged out successfully"
}
```

---

### List Users

**GET** `/api/users/`

**Query Parameters (optional):**
- `id`: Filter by user ID

**Response:**
```json
[
  {
    "id": "integer",
    "username": "string",
    "email": "string",
    "image_url": "string"
  }
]
```

---

## Job APIs

### List and Create Jobs

**GET** `/api/jobs/`

**Query Parameters (optional):**
- `category`: Filter by category ID
- `employer`: Filter by employer ID

**Response:**
```json
[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "category": "integer",
    "employer": "integer"
  }
]
```

**POST** `/api/jobs/`

**Headers:**
```
Authorization: Token <your_token>
```

**Request Body:**
```json
{
  "title": "string",
  "description": "string",
  "category": "integer"
}
```

**Response:**
```json
{
  "success": "Job list created successfully"
}
```

---

### Job Details

**GET** `/api/jobs/<int:pk>/`

**Response:**
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "category": "integer",
  "employer": "integer"
}
```

---

### Apply for a Job

**POST** `/api/jobs/<int:job_id>/apply/`

**Headers:**
```
Authorization: Token <your_token>
```

**Request Body:**
```json
{
  "cover_letter": "string (optional)"
}
```

**Response:**
```json
{
  "id": "integer",
  "job": "integer",
  "applicant": "integer",
  "status": "applied"
}
```

---

## Employer APIs

### Employer Dashboard

**GET** `/api/employer/dashboard/`

**Headers:**
```
Authorization: Token <your_token>
```

**Response:**
```json
[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "category": "integer"
  }
]
```

---

### Update Job Details

**PUT** `/api/employer/job/<int:pk>/`

**Headers:**
```
Authorization: Token <your_token>
```

**Request Body:**
```json
{
  "title": "string",
  "description": "string",
  "category": "integer"
}
```

**Response:**
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "category": "integer"
}
```

---

### View Job Applicants

**GET** `/api/employer/job/<int:job_id>/applicants/`

**Headers:**
```
Authorization: Token <your_token>
```

**Response:**
```json
[
  {
    "id": "integer",
    "applicant": "integer",
    "status": "applied"
  }
]
```

---

## Job Seeker APIs

### Job Seeker Dashboard

**GET** `/api/job-seeker/dashboard/`

**Headers:**
```
Authorization: Token <your_token>
```

**Response:**
```json
[
  {
    "id": "integer",
    "job": "integer",
    "status": "applied"
  }
]
```

---

### Update Job Seeker Details

**PUT** `/api/job-seeker/dashboard/<int:pk>/`

**Headers:**
```
Authorization: Token <your_token>
```

**Request Body:**
```json
{
  "status": "string"
}
```

**Response:**
```json
{
  "id": "integer",
  "job": "integer",
  "status": "updated_status"
}
```

---

## Categories API

### List and Create Categories

**GET** `/api/categories/`

**Response:**
```json
[
  {
    "id": "integer",
    "name": "string"
  }
]
```

**POST** `/api/categories/`

**Request Body:**
```json
{
  "name": "string"
}
```

**Response:**
```json
{
  "id": "integer",
  "name": "string"
}
```

---

## Payment APIs

### Initiate Payment

**POST** `/api/users/payment/`

**Headers:**
```
Authorization: Token <your_token>
```

**Response:**
```json
{
  "GatewayPageURL": "string"
}
```

---

### Payment Success

**POST** `/api/users/payment/success/<int:id>/`

**Response:**
```json
{
  "message": "Payment successful, user upgraded to premium."
}
```

---

### Payment Failure

**POST** `/api/users/payment/fail/<int:id>/`

**Response:**
```json
{
  "message": "Payment failed."
}
```

---

## Error Handling

- **401 Unauthorized**: Authentication token missing or invalid.
- **403 Forbidden**: Permission denied for the requested action.
- **404 Not Found**: Resource does not exist.
- **400 Bad Request**: Invalid request data.

---

## Contact

For support or API-related questions, contact: [support@yourdomain.com](mailto:support@yourdomain.com).

