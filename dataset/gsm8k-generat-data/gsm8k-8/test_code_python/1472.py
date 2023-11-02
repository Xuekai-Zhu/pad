def solution():
    # Define the amount borrowed and the amount returned per month
    amount_borrowed = 6 * 10
    amount_returned = 10

    # Calculate the amount still owed after half of the borrowed money is returned
    amount_still_owed = amount_borrowed / 2

    # Calculate how much will still be owed 4 months from now
    amount_still_owed_in_4_months = amount_still_owed - (4 * amount_returned)

    result = amount_still_owed_in_4_months
    return result

print(solution())