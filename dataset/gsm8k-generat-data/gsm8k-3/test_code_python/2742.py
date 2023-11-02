def solution():
    """Henley bought 300 candies and shared them with her two brothers. However, they realized 40% of them were sour, and they had to separate those out. If they then shared the good candies equally, how many candies did each get?"""
    # Define the initial number of candies
    total_candies = 300

    # Calculate the number of sour candies
    sour_candies = total_candies * 0.4

    # Calculate the number of good candies
    good_candies = total_candies - sour_candies

    # Divide the good candies equally among the three siblings
    candies_per_person = good_candies / 3

    # Display the number of candies each person gets
    result = candies_per_person
    return result

print(solution())