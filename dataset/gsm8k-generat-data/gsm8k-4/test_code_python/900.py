def solution():
    """Mason opens the hood of his car and discovers that squirrels have been using his engine compartment to store nuts. If 2 busy squirrels have been stockpiling 30 nuts/day and one sleepy squirrel has been stockpiling 20 nuts/day, all for 40 days, how many nuts are in Mason's car?"""
    # Define the nut storage rate for each squirrel
    busy_squirrels_rate = 30
    sleepy_squirrel_rate = 20

    # Calculate the total number of nuts stored by the busy squirrels
    busy_squirrels_nuts = 2 * busy_squirrels_rate * 40

    # Calculate the total number of nuts stored by the sleepy squirrel
    sleepy_squirrel_nuts = sleepy_squirrel_rate * 40

    # Calculate the total number of nuts in Mason's car
    total_nuts = busy_squirrels_nuts + sleepy_squirrel_nuts

    result = total_nuts
    return result

print(solution())