def solution():
    """Xavier needs 84 paper plates for a housewarming party. He already has 21 green plates and 28 red plates. How many more plates should Xavier buy?"""
    # Define the number of plates Xavier already has
    green_plates = 21
    red_plates = 28

    # Define the total number of plates Xavier needs
    total_plates_needed = 84

    # Calculate the number of plates Xavier still needs to buy
    plates_to_buy = total_plates_needed - green_plates - red_plates

    # Display the number of plates Xavier still needs to buy
    result = plates_to_buy
    return result

print(solution())