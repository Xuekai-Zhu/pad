def solution():
    """Travis has 10000 apples, and he is planning to sell these apples in boxes. Fifty apples can fit in each box. If he sells each box of apples for $35, how much will he be able to take home?"""
    # Define the number of apples and the number of apples per box
    apples = 10000
    apples_per_box = 50

    # Calculate the number of boxes
    boxes = apples / apples_per_box

    # Calculate the total earnings
    earnings = boxes * 35

    result = earnings
    return result

print(solution())