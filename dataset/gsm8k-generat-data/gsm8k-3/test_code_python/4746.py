def solution():
    """Gabriel is looking at her marble sets. She sees that in the first set 10% of her marbles are broken. In the second set, 20% of the marbles are broken. The first set contains 50 marbles. The second set contains 60. How many marbles are broken in total?"""
    # Define the percentage of broken marbles in each set
    SET_1_PERCENTAGE = 0.1
    SET_2_PERCENTAGE = 0.2

    # Define the number of marbles in each set
    SET_1_COUNT = 50
    SET_2_COUNT = 60

    # Calculate the number of broken marbles in each set
    set_1_broken = SET_1_COUNT * SET_1_PERCENTAGE
    set_2_broken = SET_2_COUNT * SET_2_PERCENTAGE

    # Calculate the total number of broken marbles
    total_broken = set_1_broken + set_2_broken

    # Display the total number of broken marbles
    result = total_broken
    return result

print(solution())