def solution():
    """Henley bought 300 candies and shared them with her two brothers. However, they realized 40% of them were sour, and they had to separate those out. If they then shared the good candies equally, how many candies did each get?"""
    # Define the number of candies Henley bought
    total_candies = 300

    # Calculate the number of sour candies
    sour_candies = total_candies * 0.4
    
    # Calculate the number of good candies
    good_candies = total_candies - sour_candies
    
    # Calculate the number of candies each person gets after sharing the good candies equally
    candies_per_person = good_candies // 3

    result = candies_per_person
    return result

print(solution())