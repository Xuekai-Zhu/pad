def solution():
    """When the machine is cold, as it is in the first hour of production, it takes 6 minutes to produce each molded flower pot. Thereafter, once it is warm, it takes only 5 minutes to produce each pot. How many additional pots are produced in the last hour of the day, compared to the first?"""

    # Define the time it takes to produce a pot when cold and warm
    COLD_TIME = 6
    WARM_TIME = 5

    # Define the number of pots produced in the first and last hour
    first_hour_pots = 10
    last_hour_pots = 15

    # Calculate the time it takes to produce the pots in the first and last hour
    first_hour_time = first_hour_pots * COLD_TIME
    last_hour_time = last_hour_pots * WARM_TIME

    # Calculate the difference in the number of pots produced
    additional_pots = round((first_hour_time - last_hour_time) / (WARM_TIME - COLD_TIME))

    # Display the additional pots produced in the last hour
    result = additional_pots
    return result

print(solution())