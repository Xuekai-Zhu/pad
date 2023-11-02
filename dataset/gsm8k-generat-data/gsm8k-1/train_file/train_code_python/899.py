def solution():
    """Mason opens the hood of his car and discovers that squirrels have been using his engine compartment to store nuts. If 2 busy squirrels have been stockpiling 30 nuts/day and one sleepy squirrel has been stockpiling 20 nuts/day, all for 40 days, how many nuts are in Mason's car?"""
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