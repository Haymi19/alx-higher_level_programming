-- Script that lists all cities of CA in the database in ascending order.
SELECT id, name FROM cities
 WHERE state_id IN
       (SELECT id
	  FROM states
	 WHERE name = "California")
 ORDER BY id;
