def solution():

    initial_number_of_swans = 15
    number_of_years = 10
    number_of_swans_doubled = 2
    number_of_swans_after_doubling = initial_number_of_swans * number_of_swans_doubled
    
    number_of_swans_after_ten_years = number_of_swans_after_doubling ** number_of_years
    
    result = number_of_swans_after_ten_years
    
    return result

print(solution())