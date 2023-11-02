def solution():
    """John earned $18 on Saturday but he only managed to earn half that amount on Sunday. He earned $20 the previous weekend. How much more money does he need to earn to give him the $60 he needs to buy a new pogo stick?"""
    # Define the earnings on Saturday, Sunday, and the previous weekend
    sat_earnings = 18
    sun_earnings = sat_earnings / 2
    prev_weekend_earnings = 20

    # Calculate the total earnings so far
    total_earnings = sat_earnings + sun_earnings + prev_weekend_earnings

    # Calculate the remaining amount needed to buy the pogo stick
    remaining_amount = 60 - total_earnings

    # return the result
    result = remaining_amount
    return result

print(solution())