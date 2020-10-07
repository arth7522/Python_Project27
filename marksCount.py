#marks count


q1 = int(input('Quiz 1 (20 Marks) : '))
mid = int(input('Mid Sem (50 Marks) : '))
q2 = int(input('Quiz 2 (20 Marks) : '))
end = int(input('End Sem (100 Marks) : '))
lab = int(input('Lab Work (100 Marks) : '))
pro = int(input('Project (50 Marks) : '))
gpa = (q1/40)+((mid*2)/50)+(q2/40)+((end*3)/100)+((lab*2)/100)+((pro*2)/50)
print('GPA : {:.2f}'.format(gpa))
