def solution():
    """When the machine is cold, as it is in the first hour of production, it takes 6 minutes to produce each molded flower pot. Thereafter, once it is warm, it takes only 5 minutes to produce each pot. How many additional pots are produced in the last hour of the day, compared to the first?"""
    # Define the production time for a cold machine and a warm machine
    COLD_TIME = 6
    WARM_TIME = 5

    # Calculate the number of pots produced in the first hour
    first_hour_pots = 60 // COLD_TIME

    # Calculate the number of pots produced in the last hour
    last_hour_pots = 60 // WARM_TIME

    # Calculate the additional pots produced in the last hour compared to the first
    additional_pots = last_hour_pots - first_hour_pots

    # return the result
    result = additional_pots
    return result

print(solution())