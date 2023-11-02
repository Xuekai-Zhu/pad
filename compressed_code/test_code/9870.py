def solution():
    
    candy_bar_price = 2
    chip_price = 0.5
    num_students = 5
    candy_bars_per_student = 1
    chips_per_student = 2
    total_cost = (candy_bar_price * candy_bars_per_student + chip_price * chips_per_student) * num_students
    result = total_cost
    return result

print(solution())