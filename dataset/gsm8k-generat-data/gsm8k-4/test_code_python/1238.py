def solution():
    """There are 3 boxes of cereal. One box holds 14 ounces of cereal. Another box holds half the amount of the first box and 5 ounces less than the third box. How much cereal is there in all 3 cereal boxes?"""
    # Define the amount of cereal in the first box
    box1 = 14

    # Define the amount of cereal in the second box (half of box1 - 5)
    box2 = box1/2 - 5

    # Define the amount of cereal in the third box (box2 + box1)
    box3 = box2 + box1

    # Calculate the total amount of cereal in all 3 boxes
    total_cereal = box1 + box2 + box3

    # Return the result
    result = total_cereal
    return result

print(solution())