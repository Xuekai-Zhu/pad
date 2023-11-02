def solution():
    burgers = 5
    burger_slices = 2 * burgers
    first_second_friends = 1 + 2
    third_fourth_friends = 3 + 3
    eaten_slices = first_second_friends + third_fourth_friends
    result = burger_slices - eaten_slices
    
    return result

print(solution())