def solution():
    """Era had 5 burgers for her and her 4 friends. She sliced each burger into halves. The first and second friends got 1 and 2 slices, respectively. Then the third and fourth friends got 3 slices each. How many slices of burgers are left for Era?"""
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