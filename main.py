#Error Handling 
#Make Readme 

while True: 
    try: 
        age = int(input('what is your age?'))
        10/age
    except ValueError: 
        print('please enter a number')
    except ZeroDivisionError: 
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break 
    finally: 
        print('ok, I am finally done')
        
        #This is from ztm course 
