def solution():
    """A phone factory makes twice as many phones as last year. Last year’s production was 5000 phones. If a quarter of this year’s production is sold, how many phones are left in the factory?"""
    # Define last year's production
    last_year_production = 5000

    # Calculate this year's production
    this_year_production = last_year_production * 2

    # Calculate the number of phones sold
    phones_sold = this_year_production / 4

    # Calculate the remaining number of phones in the factory
    remaining_phones = this_year_production - phones_sold

    # Display the remaining number of phones in the factory
    result = remaining_phones
    return result

print(solution())