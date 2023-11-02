def solution():
    """Christina's age will be half of 80 years in five years to come. If Oscar will be 3/5 times as old as Christina is now in 15 years, calculate Oscar's age now."""
    # Define Christina's current age
    christina_now = None

    # Define Oscar's current age
    oscar_now = None

    # Calculate Christina's age in 5 years
    christina_5_years = 40

    # Calculate Christina's current age
    christina_now = christina_5_years - 5

    # Calculate Oscar's age in 15 years
    oscar_15_years = (3/5) * christina_now + 15

    # Calculate Oscar's current age
    oscar_now = oscar_15_years - 15

    result = round(oscar_now)
    return result

print(solution())