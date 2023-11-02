def solution():
    # Calculate the total number of acres planted by each crew
    first_crew_acres = 2 * 2 * x  # 2 tractors working for 2 days
    second_crew_acres = 7 * 3 * x  # 7 tractors working for 3 days

    # Calculate the total acres planted in 5 days
    total_acres_planted = 1700

    # Calculate the number of acres that each tractor needs to plant per day
    tractors_needed = (total_acres_planted - first_crew_acres - second_crew_acres) / (5 * x)
    result = tractors_needed
    return result

print(solution())