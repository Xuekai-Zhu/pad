def solution():
    num_busy_squirrels = 2
    busy_squirrel_nuts_per_day = 30

    num_sleepy_squirrels = 1
    sleepy_squirrel_nuts_per_day = 20

    num_days = 40

    # Calculate the total number of nuts stockpiled by the busy squirrels
    total_busy_squirrel_nuts = num_busy_squirrels * busy_squirrel_nuts_per_day * num_days

    # Calculate the total number of nuts stockpiled by the sleepy squirrel
    total_sleepy_squirrel_nuts = num_sleepy_squirrels * sleepy_squirrel_nuts_per_day * num_days

    # Calculate the total number of nuts in Mason's car
    total_nuts = total_busy_squirrel_nuts + total_sleepy_squirrel_nuts
    result = total_nuts
    return result

print(solution())