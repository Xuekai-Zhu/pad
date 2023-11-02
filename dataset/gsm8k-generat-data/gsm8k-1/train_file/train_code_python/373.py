def solution():
    """There are 40 more buyers in the grocery store today than yesterday.
    There were half the number of buyers yesterday as there were the day before, and the day before had 50 buyers.
    Nobody visited the store on more than one day.
    What's the total number of buyers who've visited the store in the three days?"""
    
    day_one_buyers = 50
    day_two_buyers = day_one_buyers / 2
    day_three_buyers = day_two_buyers + 40
    total_buyers = day_one_buyers + day_two_buyers + day_three_buyers
    result = total_buyers
    
    return result

print(solution())