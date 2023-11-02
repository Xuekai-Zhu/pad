def solution():
    
    num_burgers = 5
    slices_per_burger = 2
    total_slices = num_burgers * slices_per_burger
    first_friend_slices = 1
    second_friend_slices = 2
    third_friend_slices = 3
    fourth_friend_slices = 3

    total_slices_given = (
        first_friend_slices +
        second_friend_slices +
        third_friend_slices +
        fourth_friend_slices
    )
    remaining_slices = total_slices - total_slices_given

    result = remaining_slices
    return result

print(solution())