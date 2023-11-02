def solution():
    """Henley bought 300 candies and shared them with her two brothers. However, they realized 40% of them were sour, and they had to separate those out. If they then shared the good candies equally, how many candies did each get?"""
    total_candies = 300
    sour_candies = total_candies * 0.4
    good_candies = total_candies - sour_candies
    num_people = 3
    good_candies_per_person = good_candies // num_people
    result = good_candies_per_person
    return result

print(solution())