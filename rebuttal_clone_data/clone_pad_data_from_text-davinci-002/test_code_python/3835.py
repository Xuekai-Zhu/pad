def solution():
    
    original_mice = 8
    pups_per_mouse = 6
    mice_after_first_litter = original_mice * pups_per_mouse
    mice_after_second_litter = mice_after_first_litter * pups_per_mouse
    mice_eaten = mice_after_second_litter / 2
    result = mice_after_second_litter - mice_eaten
    
    return result

print(solution())