def solution():
    """Lionel went to the grocery store and bought 14 boxes of Graham crackers and 15 packets of Oreos. To make an Oreo cheesecake, Lionel needs 2 boxes of Graham crackers and 3 packets of Oreos. After making the maximum number of Oreo cheesecakes he can with the ingredients he bought, how many boxes of Graham crackers would he have left over?"""
    # Define the initial number of Graham crackers and Oreos
    initial_graham_crackers = 14
    initial_oreos = 15

    # Calculate the maximum number of cheesecakes that can be made with the available ingredients
    max_cheesecakes = min(initial_graham_crackers // 2, initial_oreos // 3)

    # Calculate the number of Graham crackers left over after making the maximum number of cheesecakes
    leftover_graham_crackers = initial_graham_crackers - (max_cheesecakes*2)

    result = leftover_graham_crackers
    return result

print(solution())