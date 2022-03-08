Name:Vijay Ganesh Panchapakesan
Uta_Id:1001861777
Language used:Python
							Assignment-1 Part-1
----------------------------------------------------------------------------------------------------


Command structure:

python find_route.py input_filename origin_city destination_city [heuristic_filename]

eg:python find_route.py input1.txt Luebeck Munich 

----------------------------------------------------------------------------------------------------

Folder Structure:
1)input1.txt-It is the input file and it contains multiple rows and each row has 3 things
	I)The starting city
	II)The destination City
	III)The distance between the starting city and the destination city
  Each file should have "END OF INPUT".Failing of which will throw an error.
2)h_kassel.txt:It is the sample Hueristic file for finding route from any city to Kassel.If this file is
  given then the program will perform A* search if not then it will perform Graph search with UCS statergy
3)find_route.py:This is the main python code which finds the route from any start city to any city and prints
  them on to the console.I have used either UCS with graph serach or A* Search for finding the route between
  any two cities.
----------------------------------------------------------------------------------------------------

Functions in find_route.py:

This find_route.py has a Node which has parent,state,g(n),depth,f(n),isUninformed Bool.
The heart of this program lies in 4 main functions:
1)ReadFile:This function is used to create a dictionary of the cities based on the data in the input file
2)ReadHueresticFile:This function is used to create a dictionary of the cities and their distance based
  on the Huerestic data in the Huerestic file.
3)Expand:This function  is used to create the successors of the current node and creates a sucessorfunction
  Then this sucessorfunction is then added to the fringe in the main() after sorting the values based on g(n)
  only if this state is not in closed set
4)Route:This function is used to generate the route by following the current node's parent until the parent 
  is null.Then we need to reverse this to get the correct route.
----------------------------------------------------------------------------------------------------

How to Run the code:

Before Running please install Python 3.X into your sysytem and perfom the below steps.

Keep all the files of AI_Project_Part_1 in the same folder and run the command prompt in the place
where all the files are present and run the command in the followiung format:

For Graph search with UCS:
python find_route.py input_filename origin_city destination_city

eg:-python find_route.py input1.txt Luebeck Munich

For A* Search:
python find_route.py input_filename origin_city destination_city heuristic_filename
eg:- python find_route.py input1.txt Luebeck Munich h_kassel.txt




   
