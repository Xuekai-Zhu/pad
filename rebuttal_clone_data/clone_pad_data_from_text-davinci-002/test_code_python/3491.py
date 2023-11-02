def solution():
    cup = 1
    tablespoons_per_cup_weak = 1
    tablespoons_per_cup_strong = 2
    number_of_cups_weak = 12
    number_of_cups_strong = 12
    total_tablespoons_weak = number_of_cups_weak * tablespoons_per_cup_weak
    total_tablespoons_strong = number_of_cups_strong * tablespoons_per_cup_strong
    result = total_tablespoons_weak + total_tablespoons_strong
    
     return result

print(solution())