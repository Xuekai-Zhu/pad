def solution():
    """Matt rode his bike away from the house, he rode a total of 1000 feet.  Along the way, he passed a stop sign that was 350 feet away from his house.  He continued his ride and passed a second sign.  After passing the second sign he road an additional 275 feet.  How many feet are between the first and second signs?"""
    # Calculate the total distance Matt rode away from his house
    total_distance = 1000

    # Calculate the distance between Matt's house and the first stop sign
    distance_to_first_sign = 350

    # Calculate the distance Matt rode after passing the first stop sign
    distance_after_first_sign = total_distance - distance_to_first_sign

    # Calculate the distance Matt rode after passing the second stop sign
    distance_after_second_sign = distance_after_first_sign - 275

    # Calculate the distance between the two stop signs
    distance_between_signs = distance_after_first_sign - distance_after_second_sign

    # Display the distance between the first and second signs
    result = distance_between_signs
    return result

print(solution())