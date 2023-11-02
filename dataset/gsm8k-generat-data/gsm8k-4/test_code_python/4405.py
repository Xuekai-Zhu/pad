def solution():
    """Matt rode his bike away from the house, he rode a total of 1000 feet. Along the way, he passed a stop sign that was 350 feet away from his house. He continued his ride and passed a second sign. After passing the second sign he road an additional 275 feet. How many feet are between the first and second signs?"""
    # Define the total distance Matt rode
    total_distance = 1000

    # Define the distance to the first stop sign
    distance_to_first_sign = 350

    # Define the distance after passing the second sign
    distance_after_second_sign = 275

    # Calculate the total distance before and after the two signs
    distance_before_signs = distance_to_first_sign
    distance_between_signs = total_distance - distance_before_signs - distance_after_second_sign

    # Return the distance between the two signs
    result = distance_between_signs
    return result

print(solution())