# Regex Query API

An asynchronous REST API that runs regex searches against meal delivery data, and saves 
user-defined queries and results in an AWS PostgreSQL relational database.

## Getting started

First clone this repository using `git clone`. Then `cd` into the directory and build 
the container using `docker build -t regex-service .`

To run the container execute:

`docker run --name regex-service -d -p 80:80 regex-service`

Check that the API is running (startup takes ~1 minute):

`docker logs regex-service`

Once the container is up and running you can execute tests against the running API with:

`docker exec regex-service pytest /app`

# Usage

To view the local interactive API web-interface allowing you to see 
queries in real-time as well as documentation visit: [http://localhost/api/v1/regex/docs](http://localhost/api/v1/regex/docs)

Alternatively the API can be called programmatically using the python `requests` library.

## Endpoints

### **GET**: `api/v1/regex/get-queries`

Returns all entries inside query database.

Parameters: 

```None```

### **POST**: `api/v1/regex/add-query`

Executes regex search query against meal delivery data and saves results to the database.

Request body description:

```
{
  "column_name": "name", # Name of column to search in meal delivery dataset
  "search_word": "Pepsi", # Word to search for in meal delivery dataset
  "query": "default", # Default query to use r'(?:^|\W){}(?:$|\W)'.format(word) - cannot be changed yet
  "save": false # Whether to save regex query results to database
}
```

Response body description:

```
{
  "regex_query": "string", # used regex query
  "search_word": "string", # used search word
  "num_outlets": 0, # number of outlets which contain word in menu
  "per_outlets": 0, # percentage of outlets which contain word in menu
  "brand_id": [
    "string" # list of brand ids which contain the word
  ]
}
```

### **PUT**: `api/v1/regex/{id}`

Updates entries inside the database with an updated entry.

Parameters: 

```id: Id of item to update```
    
Request body description:

```
{
  "regex_query": "string",
  "search_word": "string",
  "num_outlets": int,
  "per_outlets": int,
  "brand_id": [
    "string"
  ]
}
```

### **DELETE**: `api/v1/regex/{id}`

Deletes an entry from the database.

Parameters: 

    - id: Id of item to delete
