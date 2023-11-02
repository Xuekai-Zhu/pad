def solution():
    """Ali has a store that sells fruits and vegetables. He puts 23 kg of kidney apples, 37 kg of golden apples and 14 kg of Canada apples on the shelves. By noon, 36 kg of apples were sold. What is the mass of apples that he has left?"""
    # Define the initial mass of kidney, golden, and Canada apples
    kidney_apples = 23
    golden_apples = 37
    canada_apples = 14

    # Calculate the total initial mass of apples
    total_apples = kidney_apples + golden_apples + canada_apples

    # Calculate the mass of apples left after selling 36 kg
    apples_left = total_apples - 36

    # Return the result
    result = apples_left
    return result

print(solution())