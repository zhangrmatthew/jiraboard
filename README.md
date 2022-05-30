# jiraboard

## Features

-   Columns
    -   Todo
    -   Implementation
    -   Code Review
    -   Merging
    -   Done
-   Task
    -   Card
        -   Name of task
        -   Assigned to who
    -   Detailed View
        -   Date Created
        -   Date Assigned
        -   Task Description
        -   Acceptance Criteria
        -   Column - can add mouse to move functionality?
        -   Delete task
-   Authentication/Access
    -   Each person can access board by taskID input
    -   Each perosn can access board by taskID in url
    -   Login using user/password

## Data Structures

### Task

```json
{
    "id": "string",
    "name": "string",
    "assignment": "string", // User ID,
    "created": "date",
    "assignement__date": "date",
    "description": "string",
    "acceptance__criteria": "string",
    "column": "string" // column ID
}
```

### Column

```json
{
    "id": "string",
    "name": "string",
    "tasks": "Array<String>" // Task ID
}
```

### Board

```json
{
    "id": "string",
    "name": "string",
    "passwordHash": "string",
    "columns": "Array<String>", // column ID
    "users": "Array<String>" // User ID,
}
```

### Users

```json
{
    "id": "string",
    "password": "string", // hash
    "username": "string",
    "boards": "Array<String>", // Board ID
    "tasks": "Array<String>"
}
```
## API Endpoints

### Create Board

```json
{
    "username":"refactor",
    "password":"refactor"
}
```

### Get All Boards

```json
{
    <no payload>
}
```

### Get Specific Board 

```json
pass thru uri
boards/<str:id>
```

### Create User
```json
{
    "username":"test",
    "password":"test"
}
```

### Get All Users

```json
{
    <no payload>
}
```

### Get Specific User 

```json
pass thru uri
boards/<str:id>
```
