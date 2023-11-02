def solution():
    """Xavier needs 84 paper plates for a housewarming party. He already has 21 green plates and 28 red plates. How many more plates should Xavier buy?"""
    # Define the total number of plates needed
    total_plates = 84

    # Define the number of plates Xavier already has
    green_plates = 21
    red_plates = 28

    # Calculate the number of plates Xavier still needs to buy
    remaining_plates = total_plates - green_plates - red_plates

    # return the result
    result = remaining_plates
    return result

print(solution())