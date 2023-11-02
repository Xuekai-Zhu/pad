def solution():
    # Calculate the average number of people added per year in Maryville
    total_people_added = 467000 - 450000  # total number of people added between 2000 and 2005
    years_elapsed = 5  # number of years between 2000 and 2005
    average_people_added_per_year = total_people_added / years_elapsed
    result = average_people_added_per_year
    return result

print(solution())