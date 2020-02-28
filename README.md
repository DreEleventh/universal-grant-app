# Universal Grant Program

Python program that gives education grants to students based on financial information provided. The project is broken up into 4 major parts.  



## Part 4 - 

Part 4 will be designed functionally. As opposed to the previous parts, part 4 will have its functionalities broken up into functions. Each module will perform one function. 

- `menu()` - This function will present the main menu to the end user. They'll be able to select a particular option and the be presented with the interface relating to said option.  The menu function will have a level of error-checking. If the user should enter some invalid then they'll be presented with an error message and be asked to re-enter a valid option. 

  The end user will be presented with: 

  ```tex
  ------------------------------
   UL GRANT APPLICATION SYSTEM
  ------------------------------
  
  A. Input Application Details for a Student.             
  B. Display Summary of Applications.             
  C. Display Grant Awardees.             
  X. Exit
  ```

  On entering an invalid option they'll be presented with the following message: 

  ```tex
  Error!! Only options A, B, C & X are valid. Please try again:
  ```

  This functionality is facilitated by the following code: 

  ```python
  while True:
      option = input().lower()
  	while option not in ['a', 'b', 'c', 'x']:
  		print("Error message!!)
      	break
  	else:
           break
  ```

  

- `app_details()` - This function will allow the user to submit the applications for a set amount of students (25).