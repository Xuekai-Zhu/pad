def solution():
    """Peggy is moving and is looking to get rid of her record collection.
    Sammy says that he will buy all of them for 4 dollars each. Bryan is only
    interested in half of the records but will offer 6 dollars each for the half
    that he is interested in and 1 dollar each for the remaining half that he is
    not interested in with the hopes that he can resell them in bulk later.
    If Peggy has 200 records, what is the difference in profit between Sammy
    versus Bryan's deal?"""
    # Define the number of records and prices
    num_records = 200
    sammy_price = 4
    bryan_interest_price = 6
    bryan_uninterest_price = 1

    # Calculate the profits
    sammy_profit = sammy_price * num_records
    bryan_interest_records = num_records // 2
    bryan_uninterest_records = num_records - bryan_interest_records
    bryan_profit = (bryan_interest_records * bryan_interest_price) + (bryan_uninterest_records * bryan_uninterest_price)
    profit_difference = sammy_profit - bryan_profit

    # Display the profit difference
    result = profit_difference
    return result

print(solution())