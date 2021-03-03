def get_maximum_value(a,b,c):
    
    max_value = a
    if b > max_value:
        max_value = b
        if c > max_value:
            max_value = c
    elif c > max_value:
        max_value = c
    return max_value

