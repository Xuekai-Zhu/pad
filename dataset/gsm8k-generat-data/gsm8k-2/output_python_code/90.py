def solution():
    """Herman likes to feed the birds in December, January and February. He feeds them 1/2 cup in the morning and 1/2 cup in the afternoon. How many cups of food will he need for all three months?"""
    cups_per_day = 1
    days_per_month = 31
    total_cups = cups_per_day * 2 * days_per_month * 3
    result = total_cups
    return result

print(solution())