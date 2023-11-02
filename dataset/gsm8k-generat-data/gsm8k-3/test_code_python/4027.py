def solution():
    """Lionel went to the grocery store and bought 14 boxes of Graham crackers and 15 packets of Oreos. To make an Oreo cheesecake, Lionel needs 2 boxes of Graham crackers and 3 packets of Oreos. After making the maximum number of Oreo cheesecakes he can with the ingredients he bought, how many boxes of Graham crackers would he have left over?"""
    # Define the number of Graham crackers and Oreos needed to make an Oreo cheesecake
    GRAHAM_CRACKER_PER_CHEESECAKE = 2
    OREO_PER_CHEESECAKE = 3

    # Define the number of boxes of Graham crackers and packets of Oreos Lionel bought
    graham_cracker_boxes = 14
    oreo_packets = 15

    # Calculate the maximum number of Oreo cheesecakes Lionel can make with the ingredients he bought
    max_cheesecakes = min(graham_cracker_boxes // GRAHAM_CRACKER_PER_CHEESECAKE, oreo_packets // OREO_PER_CHEESECAKE)

    # Calculate the number of Graham cracker boxes left over
    graham_crackers_left = graham_cracker_boxes - max_cheesecakes * GRAHAM_CRACKER_PER_CHEESECAKE

    # Display the number of Graham cracker boxes left over
    result = graham_crackers_left
    return result

print(solution())