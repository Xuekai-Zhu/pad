def solution():
    """Amber is baking cakes for her party. She has invited 8 friends and each one will want two slices of cake. Each cake makes 6 slices. If she bakes 4 cakes, how many slices will be left over at the end if she eats three herself?"""
    num_friends = 8
    slices_per_person = 2
    slices_per_cake = 6
    num_cakes = 4
    slices_eaten = 3
    
    total_num_slices = num_friends * slices_per_person * num_cakes
    remaining_slices = total_num_slices - slices_eaten
    
    result = remaining_slices % slices_per_cake
    return result

print(solution())