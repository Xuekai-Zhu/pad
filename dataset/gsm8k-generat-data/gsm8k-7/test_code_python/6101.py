def solution():
    total_cost = 120
    amount_saved = 30
    lawn_earnings = 5 * 3  # $5 earned for every lawn, and Cary mows 3 lawns every weekend.

    # Calculate how much more money Cary needs to save.
    remaining_amount = total_cost - amount_saved

    # Calculate how many more weekends Cary needs to mow lawns.
    num_weekends = remaining_amount / lawn_earnings
    result = num_weekends
    return result

print(solution())