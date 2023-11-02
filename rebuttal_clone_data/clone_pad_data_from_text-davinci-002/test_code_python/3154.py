def solution
    number_of_pies = 3
    number_of_days = 11 
    number_of_pies_eaten = 4
    number_of_cans = 2
    total_number_of_pies = number_of_pies * number_of_days
    number_of_pies_left = total_number_of_pies - number_of_pies_eaten
    number_of_cans_needed = number_of_pies_left * number_of_cans
    result = number_of_cans_needed
    return result

print(solution())