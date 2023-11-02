def solution():
    """Lionel went to the grocery store and bought 14 boxes of Graham crackers and 15 packets of Oreos. To make an Oreo cheesecake, Lionel needs 2 boxes of Graham crackers and 3 packets of Oreos. After making the maximum number of Oreo cheesecakes he can with the ingredients he bought, how many boxes of Graham crackers would he have left over?"""
    
    graham_crackers = 14
    oreos = 15
    cheesecakes_possible = min(graham_crackers//2, oreos//3)
    graham_crackers_left = graham_crackers - cheesecakes_possible*2
    result = graham_crackers_left
    return result

print(solution())