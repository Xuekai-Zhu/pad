def solution():
    
    busy_squirrels = 2
    busy_squirrel_nuts = 30
    sleepy_squirrel_nuts = 20
    total_days = 40
    busy_squirrel_total_nuts = busy_squirrels * busy_squirrel_nuts * total_days
    sleepy_squirrel_total_nuts = sleepy_squirrel_nuts * total_days
    total_nuts = busy_squirrel_total_nuts + sleepy_squirrel_total_nuts
    result = total_nuts
    return result

print(solution())