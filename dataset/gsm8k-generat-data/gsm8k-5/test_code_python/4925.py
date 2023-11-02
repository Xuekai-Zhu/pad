def solution():
    initial_collection = 18  # Bernie has 18 postcards initially
    sold_postcards = initial_collection / 2  # Bernie sells half his postcards
    earning = sold_postcards * 15  # Bernie earns $15 for each postcard sold
    new_postcards = earning / 5  # Bernie buys new postcards for $5 each

    # Total number of postcards after all transactions
    total_postcards = initial_collection - sold_postcards + new_postcards
    result = total_postcards
    return result

print(solution())