def solution():
    num_people = 8
    contribution = 5.0
    total_pot = num_people * contribution

    # Calculate the amount for first place
    first_place = 0.8 * total_pot

    # Calculate the amount for second and third place combined
    second_third = total_pot - first_place

    # Split the amount for second and third place equally
    third_place = second_third / 2.0
    result = third_place
    return result

print(solution())