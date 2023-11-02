def solution():
    """Lionel went to the grocery store and bought 14 boxes of Graham crackers and 15 packets of Oreos. To make an Oreo cheesecake, Lionel needs 2 boxes of Graham crackers and 3 packets of Oreos. After making the maximum number of Oreo cheesecakes he can with the ingredients he bought, how many boxes of Graham crackers would he have left over?"""
    boxes_of_graham = 14
    packets_of_oreos = 15
    boxes_per_cheesecake = 2
    oreos_per_cheesecake = 3

    cheesecakes_possible = min(boxes_of_graham // boxes_per_cheesecake, packets_of_oreos // oreos_per_cheesecake)
    boxes_of_graham_left = boxes_of_graham - cheesecakes_possible * boxes_per_cheesecake

    result = boxes_of_graham_left
    return result

print(solution())