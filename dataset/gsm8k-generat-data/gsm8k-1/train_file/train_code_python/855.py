def solution():
    """Randy has some money in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. If he had $104 dollars left in his piggy bank after a year, how much money, in dollars, did he have at first?"""
    store_trips_per_month = 4
    dollars_spent_per_trip = 2
    months_in_a_year = 12
    dollars_left_after_year = 104
    total_dollars_spent = store_trips_per_month * dollars_spent_per_trip * months_in_a_year
    initial_dollars = total_dollars_spent + dollars_left_after_year
    result = initial_dollars
    return result

print(solution())