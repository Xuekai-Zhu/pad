def solution():
    """Farmer Randy has 1700 acres of cotton he needs to have planted in 5 days. With a crew of 2 tractors working for 2 days and then a crew of 7 tractors working for another 3 days, how many acres of cotton per day does each tractor need to plant to meet their planting deadline?"""
    total_acres = 1700
    total_days = 5
    first_crew_days = 2
    first_crew_tractors = 2
    second_crew_days = 3
    second_crew_tractors = 7
    first_crew_acres = first_crew_days * first_crew_tractors * x
    second_crew_acres = second_crew_days * second_crew_tractors * x
    total_acres_planted = first_crew_acres + second_crew_acres
    acres_per_day_per_tractor = total_acres_planted / (total_days * (first_crew_tractors + second_crew_tractors))
    result = acres_per_day_per_tractor
    return result

print(solution())