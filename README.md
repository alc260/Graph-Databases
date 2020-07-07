
# Assignment -- Graph Databases

### Goal
The goal of this assignment is for you to gain familiarity with Graph Databases in general, and with Neo4j and, its query language, Cypher, in particular.      
* write a Python script ('cypher4.py') that will run your solutions for the 8 queries and store the query output in a file.

### Database Model

We will use the Movies database which has the following node labels:
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


---
