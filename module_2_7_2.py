def get_multiplied_digits(n):
    str_number = str(n)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else: 
        return first * get_multiplied_digits(int(str_number[1:]))
        
    
result = get_multiplied_digits(40203)
print(result)