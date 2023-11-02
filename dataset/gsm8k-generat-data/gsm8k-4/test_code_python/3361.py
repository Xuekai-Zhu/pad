def solution():
    """Agnes is 25 years old and her daughter, Jane is 6 years old. In how many years will Agnes be twice as old as Jane?"""
    # Define Agnes' current age and Jane's current age
    agnes_age = 25
    jane_age = 6

    # Initialize the year counter
    years = 0

    # Calculate the number of years until Agnes is twice as old as Jane
    while agnes_age != jane_age * 2:
        agnes_age += 1
        jane_age += 1
        years += 1

    # Return the result
    result = years
    return result

print(solution())