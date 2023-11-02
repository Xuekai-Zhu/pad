def solution():
    """Erica lives near a lake where most locals sell fish as their main source of income, earning $20 per kg of fish. She goes out fishing today and catches twice as many fish as she caught in total in the past four months. If Erica trawled 80 kg of fish in the past four months, not including today, how much money will she have earned in the past four months including today (assuming she sells all her fish)?"""
    # Define the price per kg of fish
    fish_price = 20

    # Calculate the total amount of fish caught
    total_fish = 2 * 80

    # Calculate the total income earned from selling fish in the past four months including today
    total_income = (total_fish + 80) * fish_price

    # return the result
    result = total_income
    return result

print(solution())