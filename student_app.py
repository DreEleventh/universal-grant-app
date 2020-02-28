class StudentApp():
    """A class that builds student grant applications."""

    def __init__(self, student_name, gpa, tuition_shortfal):
        """Initializing the student application variables
        
        Arguments:
            student_name {string} -- The full name of a single student
            gpa {float} -- The students grade point average, should be between 0.0 - 4.0
            tuition_shortfal {float} -- The students tuition shortfall, this must be within a 
                               particular range for acceptance into the grant program
        """

        self.student_name = student_name.title()
        self.gpa = gpa
        self.tuition_shortfal = tuition_shortfal
        
        # ID = 'UL'+str(self.ulID)
    

    
    def gpa_eval(self):
        """Evaluates a students GPA
        """
        if self.gpa < 0.0 or self.gpa > 4.0:
            print('Application Rejected')
        else:
            print('Application Accepted')

    def tuition_eval(self):
        """Evaluates a students tuition shortfall
        """
        pass

    def display(self):
        """Displays the application for a student
        """
        # print("Application ID: {}".format(ID))
        print("Students Name: {} ".format(self.student_name))
        print("Student GPA: {}".format(self.gpa))
        print("Tuition: {}".format(self.tuition_shortfal) )



# student = StudentApp('andre mckenzie', 4.3, 45699)
# student.gpa_eval()
# student.display()