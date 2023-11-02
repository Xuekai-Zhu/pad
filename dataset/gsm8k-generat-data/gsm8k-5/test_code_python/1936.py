def solution():
    num_people = 8  # Josh and 7 friends are getting together
    amount_per_person = 5  # Each person puts in 5 dollars
    total_pot = num_people * amount_per_person  # Calculate the total amount in the pot

    # Calculate the amount for first place
    first_place_amount = 0.8 * total_pot

    # Calculate the amount for second and third place
    second_third_amount = total_pot - first_place_amount

    # Split the second and third place amount evenly
    third_place_amount = second_third_amount / 2
    result = third_place_amount
    return result

print(solution())