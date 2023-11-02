def solution():
    """When the machine is cold, as it is in the first hour of production, it takes 6 minutes to produce each molded flower pot. Thereafter, once it is warm, it takes only 5 minutes to produce each pot. How many additional pots are produced in the last hour of the day, compared to the first?"""
    first_hour_pots = 60 // 6
    remaining_hours = 7
    warmed_up_pots = (60 * remaining_hours) // 5
    additional_pots = warmed_up_pots - first_hour_pots
    result = additional_pots
    return result

print(solution())