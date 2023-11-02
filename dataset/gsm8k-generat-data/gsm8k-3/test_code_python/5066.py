def solution():
    """About 450 000 people lived in Maryville in 2000. In 2005, about 467 000 people lived in Maryville. What is the average number of people added each year?"""
    # Calculate the total number of people added between 2000 and 2005
    total_added = 467000 - 450000

    # Calculate the number of years between 2000 and 2005
    years = 2005 - 2000

    # Calculate the average number of people added each year
    avg_added_per_year = total_added / years

    # Display the average number of people added each year
    result = avg_added_per_year
    return result

print(solution())