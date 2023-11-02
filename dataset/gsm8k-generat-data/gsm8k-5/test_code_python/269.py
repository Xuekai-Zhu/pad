def solution():
    saturday_earnings = 18  # John earned $18 on Saturday
    sunday_earnings = saturday_earnings / 2  # John earned half the amount on Sunday
    previous_earnings = 20  # John earned $20 the previous weekend

    # Calculate the total earnings
    total_earnings = saturday_earnings + sunday_earnings + previous_earnings

    # Calculate how much more money John needs to earn to buy a new pogo stick
    remaining_money = 60 - total_earnings
    result = remaining_money
    return result

print(solution())