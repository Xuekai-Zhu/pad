def solution():
    total_apples = 450
    number_of_children = 33
    apples_eaten_by_children = number_of_children * 10
    apples_eaten_by_adults = total_apples - apples_eaten_by_children
    number_of_adults = apples_eaten_by_adults / 3
    result = number_of_adults
    
    return result

print(solution())