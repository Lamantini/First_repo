result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number == True:
        try:
            operand = float(input("Введіть число: "))
           
           
        except ValueError:
            print("Це не число, введіть число")
            continue
        if type(result) == float:
            
            if operator == "+":
                result += operand
                
            elif operator == "-":
                result -= operand
                
            elif operator == "*":
                result *= operand
                
            elif operator == "/":
                result /= operand
        
        else:
            result = operand
        wait_for_number = False
        print (result)
        
         
    else:
        operator = input ("Введіть оператор: ")
    
        if operator not in ("+", "-", "*", "/", "="):
            print("Це не оператор")
            continue

        if operator == "=":
            print (result)
            break
        wait_for_number = True

 