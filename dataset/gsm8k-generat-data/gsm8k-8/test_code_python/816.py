def solution():
    # Define the plates used by Matt and his son
    son_plates = 3 * 2  # 3 days * 1 plate per person
    matt_plates = son_plates  # Matt also uses 1 plate per meal
    # Define the plates used by everyone when Matt's parents join them
    all_plates = 4 * 2  # Matt, his son, and two parents
    family_plates = all_plates - 2  # Subtract the 2 plates used by Matt and his son

    # Calculate the total plates used in a week
    total_plates = matt_plates + son_plates + (3 * family_plates)  # 3 days of family meals

    result = total_plates
    return result

print(solution())