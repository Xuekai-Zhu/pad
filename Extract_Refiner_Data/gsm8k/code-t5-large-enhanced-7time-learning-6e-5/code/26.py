def solution():
    
    # Define the ratio of Darrell's age to Allen's age
    darrell_to_allen_ratio = 7/11

    # Calculate the total ratio
    total_ratio = 7 + 11

    # Calculate the total age of Darrell and Allen
    total_age = 162
    allen_age = (allen_to_darrell_ratio / total_ratio) * total_age

    # Calculate Allen's age 10 years from now
    allen_age_in_10_years = allen_age + 10

    # Display Allen's age 10 years from now
    result = allen_age_in_10_years
    return result

print(solution())