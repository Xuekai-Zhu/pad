def solution():
    
    # Define Jan's age
    jan_age = 30

    # Calculate Mark's age 2 years ago
    mark_age_2_years_ago = (jan_age / 2) + 5

    # Calculate Jean's age 2 years ago
    jean_age_2_years_ago = mark_age_2_years_ago + 2

    # Calculate Jean's age
    jean_age = jean_age_2_years_ago + 2

    # Display Jean's age
    result = jean_age
    return result

print(solution())