def solution():
    
    candy_price = 2
    chips_price = 0.5
    num_students = 5
    num_candy_bars = num_students
    num_chips_bags = 2 * num_students
    total_cost = num_candy_bars * candy_price + num_chips_bags * chips_price
    result = total_cost
    return result

print(solution())