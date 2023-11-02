def solution():
    """Farmer Randy has 1700 acres of cotton he needs to have planted in 5 days. With a crew of 2 tractors working for 2 days and then a crew of 7 tractors working for another 3 days, how many acres of cotton per day does each tractor need to plant to meet their planting deadline?"""
    total_acres = 1700
    total_days = 5
    tractors_day_one = 2
    tractors_day_two = 7
    days_on_first_crew = 2
    days_on_second_crew = 3
    total_tractor_days = (tractors_day_one * days_on_first_crew) + (tractors_day_two * days_on_second_crew)
    acres_per_day_per_tractor = total_acres / total_tractor_days
    result = acres_per_day_per_tractor
    return result

print(solution())