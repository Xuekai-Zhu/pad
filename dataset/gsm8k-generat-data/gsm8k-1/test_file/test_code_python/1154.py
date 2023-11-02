def solution():
    """The Hortex company produces bottled carrot juices. Every day it can produce 4200 bottles of these juices. Each juice can cover 20% of 1 person'ts daily energy demand. How many more bottles of juices would Hortex have to produce to be able to satisfy 100% of the daily energy needs of 2300 people?"""
    bottles_per_day = 4200
    energy_coverage_per_bottle = 0.2
    daily_energy_demand_per_person = 1
    people_to_cover = 2300
    total_daily_energy_demand = daily_energy_demand_per_person * people_to_cover
    bottles_needed = total_daily_energy_demand / (energy_coverage_per_bottle * daily_energy_demand_per_person)
    additional_bottles_needed = bottles_needed - bottles_per_day
    result = additional_bottles_needed
    return result

print(solution())