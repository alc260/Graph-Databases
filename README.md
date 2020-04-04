# Repository: template.project4
# Assignment #4 -- Graph Databases

> Course: **[CS 1656 - Introduction to Data Science](http://cs1656.org)** (CS 2056) -- Spring 2020    
> Instructor: [Alexandros Labrinidis](http://labrinidis.cs.pitt.edu) and Evangelos Karageorgos  
> Teaching Assistant: Xiaoting Li
>
> Assignment: #4
> Released: April 3, 2020
> **Due:    April 13, 2020**

### Description
This is the **fourth assignment** for the CS 1656 -- Introduction to Data Science (CS 2056) class, for the Spring 2020 semester.

### Goal
The goal of this assignment is for you to gain familiarity with Graph Databases in general, and with Neo4j and, its query language, Cypher, in particular.

---

### What to do

In this assignment you are asked to:  
* download neo4j locally,  
* download the Movies database locally,   
* provide Cypher queries that answer 8 questions, and        
* write a Python script ('cypher4.py') that will run your solutions for the 8 queries and store the query output in a file.

### Database Model

We will use the Movies database in `Recitation 10`, which has the following node labels:
* Actor  
* Director  
* Movie  
* Person  
* User  
and the following relationship types (i.e., edge labels):
* ACTS_IN  
* DIRECTED  
* FRIEND  
* RATED  

The nodes in the Movies database have a number of attributes, including the following:
* name (for Actor/Director/Person/User)  
* birthday (for Actor/Director/Person/User)  
* title (for Movie)  
* genre (for Movie)  


### Setup

You are asked to follow the installation instructions and to utilize the lab material provided through `Recitation 10`. This will enable you to have a locally running neo4j server, along with an interactive query interface. You will also be able to download the Movies database directly into neo4j.

Please note that although we will use the same database model for testing your submissions. However, it will not necessarily be identical to the one you will download.

Please note that you are asked to configure the script you submit to work without authentication (for connecting to Neo4j).


### Connecting to neo4j using Python

As part of this repository, you are provided with a sample Python script (`cypher4.py`) that connects to the local graph database (which you have established by following the previous steps).


### Queries

You are asked to provide Cypher queries that provide answers for the following questions. Note that **actors** refers to both male and female actors, unless explicitly specified otherwise.

* **[Q1]** List the first 20 actors in descending order of the number of films they acted in.  
*OUTPUT*: actor_name, number_of_films_acted_in


* **[Q2]** Find the movie with the largest cast, out of the list of movies that have a review.   
*OUTPUT*: movie_title, number_of_cast_members

* **[Q3]** Show which directors have directed movies in at least 2 different genres.  
    *OUTPUT*: director name, number of genres

* **[Q4]** The Bacon number of an actor is the length of the shortest path between the actor and Kevin Bacon in the *"co-acting"* graph. That is, Kevin Bacon has Bacon number 0; all actors who acted in the same movie as him have Bacon number 1; all actors who acted in the same film as some actor with Bacon number 1 have Bacon number 2, etc. *List all actors whose Bacon number is exactly 2* (first name, last name). You can familiarize yourself with the concept, by visiting [The Oracle of Bacon](https://oracleofbacon.org).  
*OUTPUT*: actor_name


### Output Format (ignore at your own risk!)

You are asked to store the output for running all Cypher queries by your python script in a **single** file, named `output.txt`. For each query, you should have a header line `### Q1 ###`, followed by the results of the query (one row at a time, with commas separating multiple fields). If you do not provide an answer for the query, you should still print the header line in your output file, but leave a blank line after it. Answers should be ordered by query number and separated by a blank line as well.

For example, for the following question:

Q0: show the 3 oldest actors in the database, with the oldest one first.  
*OUTPUT*: name, id

The corresponding Cypher query should be:
```
match (n:Actor) return n.name, n.id order by n.birthday ASC LIMIT 3
```

The output file should be as follows:
```
### Q0 ###
Claudia Cardinale, 4959
Oliver Reed, 936
Anthony Hopkins, 4173
```

Finally, there should be an empty line between different results.


---


### Important notes about grading
It is absolutely imperative that your python program:  
* runs without any syntax or other errors (using Python 3) -- we will run it using the following command:  
`python3 cypher4.py`  
* generates file `output.txt` with the answers of all 8 queries  
* strictly adheres to the format specifications for output, as explained above.     

Failure in any of the above will result in **severe** point loss.


### Allowed Python Libraries
You are allowed to use the following Python libraries:
```
argparse
collections
csv
glob
json
math
neo4j.v1
numpy
os
pandas
re
requests
statistics
string
sqlite3
sys
```
If you would like to use any other libraries, you must ask permission by Wednesday, April 8, 2020, using [canvas](http://canvas.pitt.edu).

---


### How to submit your assignment
For this assignment, you must use the repository that was created for you after visiting the classroom link. You need to create the  file `cypher4.py` as described above, and add other files that are needed for running your program. You need to make sure to commit your code to the repository provided.

The due date is **Mondy, April 13, 2020 (23:59pm)**  

You can submit your assignment:
* up to **24 hours later, for -5 points**, and  
* up to **48 hours later, for -15 points**.  

Our assumption is that everybody will submit on the first deadline. If you want us to grade a late submission, you need to email us at `cs1656-staff@cs.pitt.edu`


### About your github account
It is very important that:  
* Your github account can do **private** repositories. If this is not already enabled, you can do it by visiting <https://education.github.com/>  
* You use the same github account for the duration of the course.  
* You use the github account that you specified during the test assignment.    
