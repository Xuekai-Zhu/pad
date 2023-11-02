def solution():
    """Mason opens the hood of his car and discovers that squirrels have been using his engine compartment to store nuts. If 2 busy squirrels have been stockpiling 30 nuts/day and one sleepy squirrel has been stockpiling 20 nuts/day, all for 40 days, how many nuts are in Mason's car?"""
    # Define the number of busy squirrels and the number of nuts each collects per day
    BUSY_SQUIRRELS = 2
    BUSY_NUTS_PER_DAY = 30

    # Define the number of sleepy squirrels and the number of nuts each collects per day
    SLEEPY_SQUIRRELS = 1
    SLEEPY_NUTS_PER_DAY = 20

    # Define the number of days this has been going on
    DAYS = 40

    # Calculate the total number of nuts collected by busy squirrels
    busy_nuts_total = BUSY_SQUIRRELS * BUSY_NUTS_PER_DAY * DAYS

    # Calculate the total number of nuts collected by the sleepy squirrel
    sleepy_nuts_total = SLEEPY_SQUIRRELS * SLEEPY_NUTS_PER_DAY * DAYS

    # Calculate the total number of nuts in Mason's car
    total_nuts = busy_nuts_total + sleepy_nuts_total

    # Display the total number of nuts
    result = total_nuts
    return result

print(solution())