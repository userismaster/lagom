# Lagom API Documentation

## Base URL
```
Development: http://localhost:8000/api/v1
Production: TBD
```

## Authentication

### Phone Verification
```http
POST /auth/verify-phone
```

### Registration
```http
POST /auth/register
```

### Login
```http
POST /auth/login
```

## User Profile

### Get Profile
```http
GET /users/profile
```

### Update Profile
```http
PUT /users/profile
```

## Educational Content

### Courses
```http
GET /education/courses
GET /education/courses/{id}
```

### Videos
```http
GET /education/videos
GET /education/videos/{id}
```

### Podcasts
```http
GET /education/podcasts
GET /education/podcasts/{id}
```

## IELTS Tests

### Mock Tests
```http
GET /exams/mock-tests
POST /exams/mock-tests/{id}/start
POST /exams/mock-tests/{id}/submit
```

### Practice Tests
```http
GET /exams/practice
GET /exams/practice/{skill}
```

## AI Features

### Grammar Check
```http
POST /ai/grammar-check
```

### Accent Analysis
```http
POST /ai/accent-analysis
```

Note: Detailed request/response schemas will be added as endpoints are implemented.
