def solution():
    graham_crackers = 14  # Lionel bought 14 boxes of Graham crackers
    oreos = 15  # Lionel bought 15 packets of Oreos
    cheesecakes_from_graham = graham_crackers // 2  # Lionel can make this many cheesecakes from the Graham crackers
    cheesecakes_from_oreos = oreos // 3  # Lionel can make this many cheesecakes from the Oreos

    # Maximum number of cheesecakes Lionel can make with the ingredients he bought
    max_cheesecakes = min(cheesecakes_from_graham, cheesecakes_from_oreos)

    # Calculate the number of boxes of Graham crackers Lionel will have left over
    boxes_leftover = graham_crackers - (max_cheesecakes * 2)
    result = boxes_leftover
    return result

print(solution())