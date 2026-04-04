# HTTP The Study Guide

---

## 1. What is HTTP?

**HTTP** (HyperText Transfer Protocol) is a communication protocol that defines how a **client** and a **server** exchange information over the internet.

```
Client  ──── Request ────►  Server
Client  ◄─── Response ────  Server
```

| Term   | Description |
|--------|-------------|
| **HTTP**  | Standard protocol for data transfer (port **80**) |
| **HTTPS** | HTTP with encrypted communication via TLS/SSL (port **443**) |
| **DNS**   | Translates a domain name (e.g. `google.com`) into an IP address (e.g. `142.250.0.1`) |

> **Note:** HTTPS is HTTP + encryption. Always prefer HTTPS in production to protect data in transit.

---

## 2. Client, Server, and APIs

- **Client**: the one who makes a **Request** (browser, mobile app, CLI tool).
- **Server / Backend**: the one who processes the request and sends a **Response**.
- **API** (Application Programming Interface): an interface exposed by the server that the client can call to get or send data.

```
Browser (Client)
    │
    │  GET /users HTTP/1.1
    │  Host: api.example.com
    ▼
API Server (Backend)
    │
    │  HTTP/1.1 200 OK
    │  { "users": [...] }
    ▼
Browser receives data
```

### SSR vs CSR

| | SSR (Server-Side Rendering) | CSR (Client-Side Rendering) |
|---|---|---|
| **Where HTML is built** | On the server | In the browser |
| **Examples** | Next.js, Django templates | React, Vue, Angular |
| **First load** | Faster (HTML arrives ready) | Slower (JS downloads first) |

---

## 3. HTTP Methods (Verbs)

HTTP methods define the **intention** of a request.

| Method   | Purpose                           | Has Body? |
|----------|-----------------------------------|-----------|
| `GET`    | Retrieve information              | No        |
| `POST`   | Create a new resource             | Yes       |
| `PUT`    | Replace an entire resource        | Yes       |
| `PATCH`  | Update part of a resource         | Yes       |
| `DELETE` | Delete a resource                 | No        |

### Examples

```http
# Get all users
GET /users HTTP/1.1
Host: api.example.com

# Create a new user
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}

# Update only the email of user 42
PATCH /users/42 HTTP/1.1
Content-Type: application/json

{
  "email": "newemail@example.com"
}

# Delete user 42
DELETE /users/42 HTTP/1.1
```

---

## 4. How to Send Information in HTTP

There are four ways to pass data in an HTTP request:

### 4.1 URL / Path Parameters

Used to **identify a specific resource**. They are part of the URL path.

```
GET /users/42
              ▲
              └── path param: userId = 42
```

```
GET /products/electronics/keyboards
              ▲           ▲
              category    subcategory
```

### 4.2 Query Parameters

Used to **filter, sort, or paginate** results. They start after `?` and are separated by `&`.

```
GET /users?status=active&role=admin&page=2
           ▲              ▲          ▲
           filter         filter     pagination
```

> Query parameters are always **optional** by convention. They should never carry required data.

### 4.3 Headers

Used to send **metadata** about the request: authentication tokens, content type, language, etc.

```http
GET /users HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
Accept-Language: en-US
```

Common headers:

| Header          | Purpose                                 |
|-----------------|-----------------------------------------|
| `Authorization` | Send authentication token (JWT, API key)|
| `Content-Type`  | Tell the server the format of the body  |
| `Accept`        | Tell the server what format you expect  |
| `Cookie`        | Send session data                       |

### 4.4 Body / Payload

Used to **send data** when creating or updating resources. Most common format: **JSON**.

```http
POST /users HTTP/1.1
Content-Type: application/json

{
  "name": "Maria Garcia",
  "email": "maria@example.com",
  "age": 28
}
```

> `GET` and `DELETE` requests do **not** have a body.

---

## 5. REST API and CRUD

**REST** (Representational State Transfer) is an architectural style for designing APIs.

Key rule: **use resources (nouns), not actions (verbs)** in your URLs.

| Wrong (action-based) | Correct (resource-based) |
|----------------------|--------------------------|
| `POST /createUser`   | `POST /users`            |
| `GET /getUser/5`     | `GET /users/5`           |
| `POST /deleteUser/5` | `DELETE /users/5`        |

### CRUD → HTTP mapping

| Operation | HTTP Method | Endpoint         | Description              |
|-----------|-------------|------------------|--------------------------|
| Create    | `POST`      | `/users`         | Create a new user        |
| Read all  | `GET`       | `/users`         | Get list of users        |
| Read one  | `GET`       | `/users/{id}`    | Get a single user by id  |
| Update    | `PUT`       | `/users/{id}`    | Replace user data        |
| Partial   | `PATCH`     | `/users/{id}`    | Update specific fields   |
| Delete    | `DELETE`    | `/users/{id}`    | Delete a user            |

### Example API Design

```
POST   /products              → create product
GET    /products              → list all products
GET    /products/7            → get product with id=7
GET    /products?category=books&page=1  → filter + paginate
PUT    /products/7            → replace product 7
PATCH  /products/7            → partially update product 7
DELETE /products/7            → delete product 7
```

---

## 6. HTTP Status Codes

The server uses status codes to tell the client **what happened** with the request.

### 2xx: Success

| Code  | Name        | When to use                         |
|-------|-------------|-------------------------------------|
| `200` | OK          | Successful GET, PUT, PATCH, DELETE  |
| `201` | Created     | Successful POST (resource created)  |
| `204` | No Content  | Success but no body to return       |

### 4xx: Client Errors

| Code  | Name          | When to use                              |
|-------|---------------|------------------------------------------|
| `400` | Bad Request   | Malformed request, invalid data          |
| `401` | Unauthorized  | Not authenticated (no token or invalid)  |
| `403` | Forbidden     | Authenticated but no permission          |
| `404` | Not Found     | Resource does not exist                  |
| `422` | Unprocessable | Validation error on the request body     |

### 5xx: Server Errors

| Code  | Name                   | When to use                         |
|-------|------------------------|-------------------------------------|
| `500` | Internal Server Error  | Unexpected crash on the server      |
| `502` | Bad Gateway            | Server got invalid response upstream|
| `503` | Service Unavailable    | Server is down or overloaded        |

> **401 vs 403:** `401` means "who are you?" (not logged in). `403` means "I know who you are, but you can't do this."

---

## 7. Tools to Make HTTP Requests

| Tool         | Type              | Language / Platform       |
|--------------|-------------------|---------------------------|
| `fetch`      | Built-in          | JavaScript (browser/Node) |
| `axios`      | Library           | JavaScript / TypeScript   |
| `requests`   | Library           | Python                    |
| `curl`       | CLI               | Terminal (any OS)         |
| Postman      | GUI app           | Testing & documentation   |
| Swagger/OpenAPI | Documentation  | Describes API endpoints   |

### Examples

**JavaScript: fetch**
```js
const response = await fetch('https://api.example.com/users/5');
const user = await response.json();
console.log(user);
```

**JavaScript: axios**
```js
const { data } = await axios.get('/users', {
  params: { status: 'active' },
  headers: { Authorization: `Bearer ${token}` }
});
```

**Python: requests**
```python
import requests

response = requests.get(
    'https://api.example.com/users',
    params={'status': 'active'},
    headers={'Authorization': 'Bearer mytoken'}
)
print(response.json())
```

**curl: terminal**
```bash
# GET
curl https://api.example.com/users

# POST with JSON body
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'

# With auth token
curl https://api.example.com/users \
  -H "Authorization: Bearer mytoken123"
```

---

## 8. Reading API Documentation

Good API documentation always specifies:

1. **Method**: `GET`, `POST`, etc.
2. **URL / Endpoint**: `/users/{id}`
3. **Path parameters**: required, part of the URL
4. **Query parameters**: optional, after `?`
5. **Request body**: schema and required fields
6. **Response**: status code and example body
7. **Authentication**: how to send credentials

### Example documentation entry

```
GET /users/{userId}/orders

Path parameters:
  userId (required) — integer — ID of the user

Query parameters:
  status  (optional) — string  — Filter by order status: "pending" | "shipped" | "delivered"
  page    (optional) — integer — Page number, default: 1
  limit   (optional) — integer — Items per page, default: 20

Headers:
  Authorization: Bearer <token>  (required)

Response 200:
{
  "orders": [
    { "id": 1, "status": "shipped", "total": 59.99 }
  ],
  "page": 1,
  "total": 42
}

Response 404:
{ "error": "User not found" }
```
