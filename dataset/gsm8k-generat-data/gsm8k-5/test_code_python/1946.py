def solution():
    starting_amount = 200  # Randy has $200 in his piggy bank
    spent_per_trip = 2  # Randy spends $2 every time he goes to the store
    trips_per_month = 4  # Randy goes to the store 4 times per month
    months_per_year = 12  # Randy wants to know how much money he will have after a year

    # Calculate the total amount spent in a year
    spent_per_year = spent_per_trip * trips_per_month * months_per_year

    # Calculate the final amount in Randy's piggy bank after a year
    final_amount = starting_amount - spent_per_year
    result = final_amount
    return result

print(solution())