# PatientDatabase
Simple Database Manipulation Project - Adding/Deleting Entities Using Python, Flask, Bootstrap, HTML, Javascript.

README
This document contains information and instructions on how to use my web application.
The purpose of this project was for me to practic and get familiar with building a web application.

Author: Hana Wahi
Email: HQW5245@psu.edu


To start up my web app, follow the following instructions:
- Open PYCHARM and hit green arrow near the bottom.
- Open web browser and navigate to specified host. (http://127.0.0.1:5000/)
- The Home/Index page of my web application should be there.

To use the program:
- Utilize the dropdown menu to select an action. ("Delete Patients" or "Add Patients" to and from database.)
- Hit "Go!" to navigate to corresponding action pages. When either page is accessed, an up-to-date table representation of our current database will appear!
Adding Patients:
- After navigating to "Add Patients" page via the dropdown menu and "Go!" button:
- Enter a first and last name to insert into the database. Note that fields MUST be filled before being allowed to continue.
- Hit Insert; a modal entitled "Insertion Confirmation" will pop up. Select "Continue" to continue insertion, or "No" to close the pop-up.
- The table will refresh after Continueing, and be up-to-date. The newly added patient will have a unique PID!
- Hit "Go Back" to return back to the Home/Index page.
Deleting Patients:
- After navigating to Delete Patients" page via the dropdown menu and "Go!" button:
- Enter a first and last name to delete from the database. Note that fields MUST be filled before being allowed to continue.
- Hit Delete; a modal entitled "Deletion Confirmation" will pop up. Select "Delete" to continue deletion, or "No" to close the pop-up.
- The table will refresh after Deleting, and be up-to-date.
- Hit "Go Back" to return back to the Home/Index page.

FUNCTION DESCRIPTIONS:
In app.py, you will find several functions. Below they are listed with a brief description.
@app.routes:
- @app.route('/')
	This routes the application to the index. Simply renders/returns my homepage, 'index.html'.
- @app.route('/select', methods=['POST'])
	This first updates the "cursor", which will hold the latest SQL data. If a table doesn't 
	exist, it creates one. It then routes the application to "delete.html" or "input.html", for
	deletion or insertion (respectively), depending on which drop-down option was selected upon
	the user hitting "Go!" submission. If neither is selected, it just routes the application to
	the index page.
- @app.route('/name', methods=['POST', 'GET'])
	This routes the application to attempt to insert/add the name from the database. It uses function
	"valid_name" (description below); before this, it checks to see if it is valid ("if result"; check
	to see if anything is in this variable), and if it is, it is inserted into the table.
- @app.route('/delete', methods=['POST', 'GET'])
	This routes the application to attempt to delete/remove the name from the database. It uses function
	"valid_name_delete" (description below); before this, it checks to see if it is valid ("if result"; 
	checks to see if anything is in this variable), and if it is, it is deleted from the table (if it exists).
Function Definitions:
- def valid_name(first_name, last_name)
	This function is for inserting values into the table. It first checks to see if the table exists. If
	it doesn't, the table is created. Then, the function inserts the values into the table, given the values
	passed to it (first_name, last_name). For each value inserted into the database, a new and unique PID
	is assigned to the value using SqLite's autoincrement feature. The function returns the latest updated table.
- def valid_name_delete(first_name, last_name)
	This function is for deleting values from the table. It first checks to see if the table exists. If
	it doesn't, the table is created. Then, the function attempts to delete the value from the table, given
	the values passed to it (first_name, last_name). If the value is not found, no foul; the function returns
	the latest table.


Sources:
https://html.com/tags/comment-tag/
StackOverFlow
w3Schools
