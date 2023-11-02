def solution():
    """Ali has a store that sells fruits and vegetables. He puts 23 kg of kidney apples, 37 kg of golden apples and 14 kg of Canada apples on the shelves. By noon, 36 kg of apples were sold. What is the mass of apples that he has left?"""
    # Define the initial masses of each type of apple
    kidney_mass = 23
    golden_mass = 37
    canada_mass = 14

    # Calculate the total initial mass of apples
    total_initial_mass = kidney_mass + golden_mass + canada_mass

    # Subtract the mass of the sold apples
    remaining_mass = total_initial_mass - 36

    # Display the remaining mass of apples
    result = remaining_mass
    return result

print(solution())