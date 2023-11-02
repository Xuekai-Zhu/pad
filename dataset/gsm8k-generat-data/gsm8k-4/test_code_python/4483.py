def solution():
    """Peggy is moving and is looking to get rid of her record collection. Sammy says that he will buy all of them for 4 dollars each. Bryan is only interested in half of the records but will offer 6 dollars each for the half that he is interested in and 1 dollar each for the remaining half that he is not interested in with the hopes that he can resell them in bulk later. If Peggy has 200 records, what is the difference in profit between Sammy versus Bryan's deal?"""
    # Define the number of records and the price per record for each deal
    NUM_RECORDS = 200
    SAMMY_PRICE = 4
    BRYAN_INTERESTED_PRICE = 6
    BRYAN_NOT_INTERESTED_PRICE = 1

    # Calculate the profit from Sammy's deal
    sammy_profit = NUM_RECORDS * SAMMY_PRICE

    # Calculate the profit from Bryan's deal
    bryan_interested_records = NUM_RECORDS / 2
    bryan_not_interested_records = NUM_RECORDS / 2
    bryan_profit = bryan_interested_records * BRYAN_INTERESTED_PRICE + bryan_not_interested_records * BRYAN_NOT_INTERESTED_PRICE

    # Calculate the difference in profit between the two deals
    profit_difference = bryan_profit - sammy_profit

    # Return the result
    result = profit_difference
    return result

print(solution())