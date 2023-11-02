def solution():
    num_students = 5
    candy_bar_price = 2
    chips_price = 0.5
    num_candy_bars = num_students
    num_chips = num_students * 2

    # Calculate the total cost of all candy bars
    total_candy_bar_cost = num_candy_bars * candy_bar_price

    # Calculate the total cost of all chips
    total_chips_cost = num_chips * chips_price

    # Calculate the total cost for all students
    total_cost = total_candy_bar_cost + total_chips_cost
    result = total_cost
    return result

print(solution())