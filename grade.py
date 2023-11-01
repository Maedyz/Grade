def quiz_calculation(list):
    # hazv kamtarin nomre ha
    rang = 6
    for a in range(2):        
        index = 0
        min = 100
        for i in range(rang):
            if min > int(list[i]):
                min = int(list[i])
                index = i                 
        list.pop(index)
        rang -= 1
    
    # miangin
    sum = 0
    for a in range(4):
        sum += int(list[a])        
    return sum / 4

def example_calculation(list):
    # hazv kamtarin nomre      
    index = 0
    min = 100
    for i in range(4):
        if min > int(list[i]):
            min = int(list[i])
            index = i                 
    list.pop(index)
    
    # miangin
    sum = 0
    for a in range(3):
        sum += int(list[a])        
    return sum / 4
    
               

def my_final_grade_calculation(filename):
    try:        
        file1 = open(filename,"r+")
    except: 
        print("File Error!!")
        return
    
    students = file1.readlines()
    dic = {}
    for student in students:
        try:           
            list = student.split(',')        
            name = list[0]
            q1 = list[1]
            q2 = list[2]
            q3 = list[3]
            q4 = list[4]
            q5 = list[5]
            q6 = list[6]
            a1 = list[7]
            a2 = list[8]
            a3 = list[9]
            a4 = list[10]
            midterm = int(list[11])
            final = int(list[12])
            
            quiz_grade = quiz_calculation([q1,q2,q3,q4,q5,q6])
            example_grade = example_calculation([a1,a2,a3,a4])
            grade = (quiz_grade + example_grade + midterm + final) / 4
            
            if grade > 60:
                dic.update({name.lower():"pass"})
            else:
                dic.update({name:"faild"})                              
        
        except:
            print("List Error!!")
        
                
    return dic    
        
        
print(my_final_grade_calculation("file.txt"))