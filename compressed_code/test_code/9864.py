def solution():
    
    burgers = 5
    slices_per_burger = 2
    
    
    first_two_friends = 1 + 2
    
    third_fourth_friends = 3 + 3
    total_slices_eaten = first_two_friends + third_fourth_friends
    
    
    remaining_slices = (burgers * slices_per_burger) - total_slices_eaten
    result = remaining_slices
    
    return result

print(solution())