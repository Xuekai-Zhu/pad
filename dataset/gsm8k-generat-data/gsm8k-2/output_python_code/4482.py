def solution():
    """Peggy is moving and is looking to get rid of her record collection. Sammy says that he will buy all of them for 4 dollars each. Bryan is only interested in half of the records but will offer 6 dollars each for the half that he is interested in and 1 dollar each for the remaining half that he is not interested in with the hopes that he can resell them in bulk later. If Peggy has 200 records, what is the difference in profit between Sammy versus Bryan's deal?"""
    record_count = 200
    sammy_price = 4
    bryan_interested_count = record_count / 2
    bryan_interested_price = 6
    bryan_not_interested_count = record_count / 2
    bryan_not_interested_price = 1

    sammy_profit = sammy_price * record_count
    bryan_profit = (bryan_interested_count * bryan_interested_price) + (bryan_not_interested_count * bryan_not_interested_price)

    profit_difference = bryan_profit - sammy_profit
    result = profit_difference
    return result

print(solution())