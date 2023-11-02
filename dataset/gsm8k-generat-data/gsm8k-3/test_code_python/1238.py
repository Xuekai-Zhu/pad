def solution():
    """There are 3 boxes of cereal. One box holds 14 ounces of cereal. Another box holds half the amount of the first box and 5 ounces less than the third box. How much cereal is there in all 3 cereal boxes?"""
    # Define the amount of cereal in the first box
    box1_cereal = 14

    # Calculate the amount of cereal in the second box
    box2_cereal = box1_cereal / 2 - 5

    # Define the amount of cereal in the third box
    box3_cereal = box2_cereal + 5

    # Calculate the total amount of cereal in all three boxes
    total_cereal = box1_cereal + box2_cereal + box3_cereal

    # Display the total amount of cereal
    result = total_cereal
    return result

print(solution())