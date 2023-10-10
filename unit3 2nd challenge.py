def CgpaCalc(marks, n): 
 

    # Variable to store the grades in 

    # every subject 

    grade = [0] * n

   

    # Variables to store CGPA and the 

    # sum of all the grades 

    Sum = 0

   

    # Computing the grades 

    for i in range(n):

       grade[i] = (marks[i] / 10)

   

    # Computing the sum of grades 

    for i in range(n):

       Sum += grade[i]

   

    # Computing the CGPA 

    cgpa = Sum / n