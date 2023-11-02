def solution():
    """There are 40 more buyers in the grocery store today than yesterday. There were half the number of buyers yesterday as there were the day before, and the day before had 50 buyers. Nobody visited the store on more than one day. What's the total number of buyers who've visited the store in the three days?"""
    # Define the number of buyers on the first day
    day1_buyers = 50

    # Calculate the number of buyers on the second day
    day2_buyers = day1_buyers / 2

    # Calculate the number of buyers on the third day
    day3_buyers = day2_buyers + 40

    # Calculate the total number of buyers
    total_buyers = day1_buyers + day2_buyers + day3_buyers

    # return the result
    result = total_buyers
    return result

print(solution())