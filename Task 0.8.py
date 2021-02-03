def time_conversion(num):
    hour = num/60
    whole = int(hour)
    minut = (hour-whole)*60
        
    if whole <= 1 and minut <= 1:
            time = f'{int(hour)} hour,{int(minut)} minute'
        
    elif whole <= 1 and minut > 1:
            time = f'{int(hour)} hour,{int(minut)} minutes'
        
    elif whole > 1 and minut <= 1:
            time = f'{int(hour)} hours,{int(minut)} minute'
        
    elif whole > 1 and minut > 1:
            time = f'{int(hour)} hours,{int(minut)} minutes'
        
    return (time)

converted_time = time_conversion(133)
print(converted_time)