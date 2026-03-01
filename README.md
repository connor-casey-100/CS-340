# CS-340

How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
 - To write programs that are maintainable, readable, and adaptable, I utilized the concept of modularization and encapsulation. By separating the database operations into their own class file, I ensured that the Dashboard application code remainedclean and focused solely on the user interface and callback logic.
 - The primary advantage of working this way was the ease of knowing where to look when trying to debug a query or encountering issues with DB connection.
 - Furthermore, this approach makes the code highly adaptable and reusable. In the future, this same CRUD module could be imported into a completely different application without needing to rewrite a single line of the database logic.

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
 - As a computer scientist, I approached the Grazioso Salvare project by decomposing the client's high level requirements into smaller, solvable technical components. For instance, the client requested the ability to find dogs for "Water Rescue".
 - I translated this into a query filtering for their requirements: "Intact Female", specific breeds like "Newfoundland", and an age range of 26-156 weeks.
 - My approach differed from previous assignments because it required handling real-world data.
 - In the future, I would continue to use this strategy of iterative testing to ensure robust solutions for client requests.

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
 - Computer scientists act as the bridge between raw data and actionable human insight.
 - In the context of Grazioso Salvare, my work transforms a static, overwhelming database of hundreds of animal records into a dynamic decision-making tool.
 - By automating the filtering process and visualizing the data, I am enabling the client to work significantly faster and more accurately.
 - Ultimately, this efficiency matters because it allows Grazioso Salvare to focus their resources on training and rescue operations rather than administrative data entry.
