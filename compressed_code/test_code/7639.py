def solution():
    
    slices_per_loaf = 15
    num_loaves = 4
    num_friends = 10
    total_slices = slices_per_loaf * num_loaves
    slices_per_friend = total_slices / num_friends
    result = slices_per_friend
    return result

print(solution())