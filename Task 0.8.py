def time_conversion(num):
    hour = num/60
    whole = int(hour)
    minut = (hour-whole)*60
        
    if whole == 0 and minut == 0:
        time = f'{int(hour)} hours,{int(minut)} minutes'
    
    elif whole <= 1 and minut <= 1:
            time = f'{int(hour)} hour,{int(minut)} minutes'
        
    elif whole <= 1 and minut >= 0:
            time = f'{int(hour)} hour,{int(minut)} minutes'
        
    elif whole > 1 and minut <= 1:
            time = f'{int(hour)} hours,{int(minut)} minutes'
        
    elif whole > 1 and minut >= 0:
            time = f'{int(hour)} hours,{int(minut)} minutes'
    return (time)

converted_time = time_conversion(0)
print(converted_time)