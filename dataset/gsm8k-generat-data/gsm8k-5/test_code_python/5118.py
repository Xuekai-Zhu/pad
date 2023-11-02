def solution():
    # Marigolds sold on day 1
    sold_day1 = 14

    # Marigolds sold on day 2
    sold_day2 = sold_day1 + 25

    # Marigolds sold on day 3
    sold_day3 = sold_day2 * 2

    # Total marigolds sold during the sale
    total_sold = sold_day1 + sold_day2 + sold_day3
    result = total_sold
    return result

print(solution())