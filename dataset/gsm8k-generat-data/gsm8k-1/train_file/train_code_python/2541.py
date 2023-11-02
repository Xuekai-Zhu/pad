def solution():
    """When the machine is cold, as it is in the first hour of production, it takes 6 minutes to produce each molded flower pot. Thereafter, once it is warm, it takes only 5 minutes to produce each pot. How many additional pots are produced in the last hour of the day, compared to the first?"""
    cold_production_time = 60
    warm_production_time = 240
    cold_time_per_pot = 6
    warm_time_per_pot = 5
    cold_pots = cold_production_time // cold_time_per_pot
    warm_pots = warm_production_time // warm_time_per_pot
    additional_pots = warm_pots - cold_pots
    result = additional_pots
    return result

print(solution())