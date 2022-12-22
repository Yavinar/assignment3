"""4. Write a program to prompt the user for a grade between 4 and 10. If the grade
is out of range print error message. If the grade is between 4 and 10 Print the
grade and the performance using the following:
Letter Grade Performance Grade Points
A+  Outstanding     10
A   Excellent   9
B+  Very Good   8
B   Good        7
C+  Average     6
C   Below Average 5
D   Poor        4

E.g.: For Grade 9 Output is:
Your Grade is ‘A’ and Excellent Performance."""



grade_point=int(input("Enter grade points:"))
dic={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#Applying Conditions for correct grade range
if 4<=grade_point<=10:
        statement=dic.get(grade_point)
        print(statement)
else:
       print("\nError\nPlease enter grade in range [4,10]")