def solution():
    """Era had 5 burgers for her and her 4 friends. She sliced each burger into halves. The first and second friends got 1 and 2 slices, respectively. Then the third and fourth friends got 3 slices each. How many slices of burgers are left for Era?"""
    burgers = 5
    slices_per_burger = 2
    
    # Total slices eaten by first two friends
    first_two_friends = 1 + 2
    # Total slices eaten by third and fourth friends
    third_fourth_friends = 3 + 3
    total_slices_eaten = first_two_friends + third_fourth_friends
    
    # Calculate remaining slices for Era
    remaining_slices = (burgers * slices_per_burger) - total_slices_eaten
    result = remaining_slices
    
    return result

print(solution())