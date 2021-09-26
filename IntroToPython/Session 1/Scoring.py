def VariableExist(variables):
    errors = 0
    x= variables.split(',')
    for var in x:
        try: 
            globals()[var]
        except NameError: 
            print(f"NameError: {var} doens't exist")
            errors += 1
        except KeyError: 
            print(f"NameError: {var} doens't exist")
            errors += 1
    if errors == 0:
        if len(x) == 1:
            print(f"Great Work! {x} is declared correctly")
        else:
            print(f"Great Work! {x} are declared correctly")
        
    return errors   

def AllIntegers(variables):
    errors1 = VariableExist(variables)   
    x= variables.split(',')
    errors2= 0
    for var in x:
        try: 
            assert(isinstance(globals()[var],int))
        except: 
            print(f"Error: {var} is not an integer")
            errors2 += 1
    if errors2 == 0:
        print(f"Great Work! {x} is an integer")

    
    return errors1 + errors2 

def AllStrings(variables):
    errors1 = VariableExist(variables)   
    x= variables.split(',')
    errors2= 0
    for var in x:
        try: 
            assert(isinstance(globals()[var],str))
        except: 
            print(f"Error: {var} is not a string")
            errors2 += 1
    if errors2 == 0:
        print(f"Great Work! {x} is a string")

    
    return errors1 +errors2 

def TaskTwo(value,num,remainder):
    value = 456723
    errors = 0
    if num == 2 and remainder == 1:
        print(f"Your answer is correct and {value} is odd")
    elif num != 2 and remainder ==1:
        print("Error: num value is wrong")
        errors = 1
    elif num == 2 and remainder !=1:
        print("Error: remainder value is wrong")
        errors = 1
    else:
        "Error: Borth remainder and num values are wrong"
        errors = 2
        
    
    return errors

def TaskThree(animalsListLength,StudentAgesLength,AgeEqual20,sortedStudentAges,OldestPerson):    
    animalsList = ["Donkey","Monkey","Lion","Camel","Goat","Whale","Fish"]
    StudentAges = [20,20,21,23,23,20,25,22,33,20,21,20] 
    errors = 0
    
    if len(animalsList) == animalsListLength:
        print("Animals List Length part         is correct")
    else:
        print("Animals List Length part         is wrong")
        errors +=1
        
    if len(StudentAges) == StudentAgesLength:
        print("Student Ages List Length part    is correct")
    else:
        print("Student Ages List Length part    is wrong")
        errors +=1
        
    if AgeEqual20 == StudentAges.count(20):
        print("Finding Studens aged 20 part     is correct")
    else:
        print("Finding Studens aged 20 part     is wrong")
        errors +=1
    
    if sortedStudentAges == sorted(StudentAges):
        print("The function sorting part        is correct")
    else:
        print("The function sorting part        is wrong")
        errors +=1
        
    if OldestPerson == max(StudentAges):
        print("The oldest person part           is correct")
    else:
        print("The oldest person part           is wrong")
        errors +=1
        
    return errors

def TaskFour(Python10):
    errors = AllIntegers("PythonLoc") + AllStrings("Python10")
    if Python10 == ("Python "*10):
        print("Great Work! Python10 is printing the correct string")
    else:
        errors +=1
        print("Error: Python10 is not printing the correct string")
        
    return errors