def solution():
    """Herman likes to feed the birds in December, January and February. He feeds them 1/2 cup in the morning and 1/2 cup in the afternoon. How many cups of food will he need for all three months?"""
    # Define the number of cups of food needed per day
    cups_per_day = 1

    # Calculate the number of cups of food needed per month
    cups_per_month = cups_per_day * 2 * 30

    # Calculate the total number of cups of food needed for all three months
    total_cups = cups_per_month * 3

    # return the result
    result = total_cups
    return result

print(solution())