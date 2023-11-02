def solution():
    """During the outbreak of the coronavirus, a company had to ramp up its toilet paper production three times more to cover the increased demand. If the company was producing 7000 toilet paper per day, calculate its total toilet paper production during March of 2020 after increasing its production."""
    # Define the company's daily production before ramping up
    daily_production_before = 7000

    # Calculate the company's daily production after ramping up
    daily_production_after = daily_production_before * 3

    # Calculate the total production for March (31 days)
    total_production = daily_production_after * 31

    # Display the total production for March
    result = total_production
    return result

print(solution())