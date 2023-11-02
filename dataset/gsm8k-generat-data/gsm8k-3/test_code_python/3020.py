def solution():
    """Erica lives near a lake where most locals sell fish as their main source of income, earning $20 per kg of fish. She goes out fishing today and catches twice as many fish as she caught in total in the past four months. If Erica trawled 80 kg of fish in the past four months, not including today, how much money will she have earned in the past four months including today (assuming she sells all her fish)?"""
    # Define the price per kilogram of fish
    PRICE_PER_KILOGRAM = 20

    # Define the total amount of fish caught in the past 4 months
    PAST_FOUR_MONTHS_FISH = 80

    # Calculate the total amount of fish caught today
    TODAY_FISH = PAST_FOUR_MONTHS_FISH * 2

    # Calculate the total amount of fish caught in the past 4 months including today
    TOTAL_FISH = PAST_FOUR_MONTHS_FISH + TODAY_FISH

    # Calculate the total amount of money earned from the fish
    TOTAL_EARNINGS = TOTAL_FISH * PRICE_PER_KILOGRAM

    # Display the total earnings
    result = TOTAL_EARNINGS
    return result

print(solution())