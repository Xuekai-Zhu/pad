def solution():
    """Cary starts working at Game Stop for $10/hour. She gets a 20% raise the first year, but the second year the company's profits decrease and her pay is cut to 75% of what it used to be. How much does Cary make now?"""
    # Define Cary's initial hourly rate
    initial_rate = 10

    # Calculate Cary's hourly rate after the first year
    first_year_rate = initial_rate * 1.2

    # Calculate Cary's hourly rate after the second year
    second_year_rate = first_year_rate * 0.75

    # Display Cary's current hourly rate
    result = second_year_rate
    return result

print(solution())