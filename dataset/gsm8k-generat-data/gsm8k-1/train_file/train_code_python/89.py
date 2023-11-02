def solution():
    """Herman likes to feed the birds in December, January and February. He feeds them 1/2 cup in the morning and 1/2 cup in the afternoon. How many cups of food will he need for all three months?"""
    cups_per_day = 1
    cups_per_month = cups_per_day * 2 * 30 # feeding for 30 days
    cups_total = cups_per_month * 3 # feeding for 3 months
    result = cups_total
    return result

print(solution())