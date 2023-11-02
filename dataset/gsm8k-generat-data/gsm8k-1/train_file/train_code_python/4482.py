def solution():
    """Peggy is moving and is looking to get rid of her record collection. Sammy says that he will buy all of them for 4 dollars each. Bryan is only interested in half of the records but will offer 6 dollars each for the half that he is interested in and 1 dollar each for the remaining half that he is not interested in with the hopes that he can resell them in bulk later. If Peggy has 200 records, what is the difference in profit between Sammy versus Bryan's deal?"""
    total_records = 200
    sammy_offer = 4
    bryan_half = total_records / 2
    bryan_interest = bryan_half * 6
    bryan_not_interest = bryan_half * 1
    bryan_offer = bryan_interest + bryan_not_interest
    sammy_profit = sammy_offer * total_records
    bryan_profit = bryan_offer - (bryan_half * 1) # subtract cost of uninterested records
    profit_difference = bryan_profit - sammy_profit
    result = profit_difference
    
    return result

print(solution())