def time_conversion(num):
    hour = num/60
    whole = int(hour)
    minut = (hour-whole)*60
        
    if whole == 0 or whole > 1:
        if minut == 0 or minut > 1:
            time = f'{int(hour)} hours, {round(minut)} minutes'
        else:
            time = f'{int(hour)} hours, {round(minut)} minute'
            
    else:
        if minut == 0 or minut > 1:
            time = f'{int(hour)} hour, {round(minut)} minutes'
        else:
            time = f'{int(hour)} hour, {round(minut)} minute'
    return time
            
converted_time = time_conversion(61)
print(converted_time)