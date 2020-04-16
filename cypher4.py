from neo4j.v1 import GraphDatabase, basic_auth
#Ava Chong

#connection with authentication
#driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "cs1656"), encrypted=False)

#connection without authentication
driver = GraphDatabase.driver("bolt://localhost", encrypted=False)

session = driver.session()
transaction = session.begin_transaction()

#result = transaction.run("MATCH (people:Person) RETURN people.name LIMIT 10")
#for record in result:
   #print (record['people.name'])

##Put assignment here

output_string = ""

#print("### Q1 ###")
output_string += "### Q1 ###\n"
result = transaction.run("MATCH (a:Actor)-[:ACTS_IN]->(i) RETURN a.name, count(DISTINCT i.title) AS Movie_count ORDER BY Movie_count DESC LIMIT 20")
for record in result:
   output_string += record['actor_name'] + "," + str(record['number_of_movies']) + "\n"
output_string += "\n"

#print("### Q2 ###")
output_string += "### Q2 ###\n"
result = transaction.run("MATCH (a:Actor)-[:ACTS_IN]->(m:Movie)<-[:RATED]-() with m, count(distinct a) AS number_of_cast_members order by number_of_cast_members desc return m.title, number_of_cast_members limit 1")
for record in result:
   output_string += record['movie_title'] + "," + str(record['number_of_cast_members']) + "\n"
output_string += "\n"

#print("### Q3 ###")
output_string += "### Q3 ###\n"
result = transaction.run("MATCH (p)-[r:DIRECTED]->(mv) with p.name as director_name, count(DISTINCT mv.genre) as number_of_genres WHERE number_of_genres >= 2 RETURN director_name, number_of_genres ORDER BY number_of_genres DESC")
for record in result:
   output_string += record['director_name'] + "," + str(record['number_of_genres']) + "\n"
output_string += "\n"

#print("### Q4 ###")
output_string += "### Q4 ###\n"

Q4 = """
MATCH (kevin:Actor {name:'Kevin Bacon'})-[:ACTS_IN]->(moo:Movie)<-[:ACTS_IN]-(people:Actor) 
MATCH (people:Actor)-[:ACTS_IN]->(moo2:Movie)<-[:ACTS_IN]-(want:Actor) WHERE kevin <> want AND NOT (kevin)-[:ACTS_IN]->()<-[:ACTS_IN]-(want) RETURN DISTINCT want.name as full_name ORDER BY full_name asc
"""
result = transaction.run(Q4)
for record in result:
   output_string += record['actor_name'] + "\n"
output_string += "\n"

with open("output.txt", "w", encoding='utf-8') as output_file:
    output_file.write(output_string)

transaction.close()
session.close()