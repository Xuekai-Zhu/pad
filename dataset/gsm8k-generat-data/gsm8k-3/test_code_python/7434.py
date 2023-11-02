def solution():
    """Travis has 10000 apples, and he is planning to sell these apples in boxes. Fifty apples can fit in each box. If he sells each box of apples for $35, how much will he be able to take home?"""
    # Define the number of apples
    NUM_APPLES = 10000

    # Define the number of apples per box and the price per box
    APPLES_PER_BOX = 50
    BOX_PRICE = 35

    # Calculate the number of boxes Travis can sell
    num_boxes = NUM_APPLES // APPLES_PER_BOX

    # Calculate Travis's earnings
    earnings = num_boxes * BOX_PRICE

    # Display Travis's earnings
    result = earnings
    return result

print(solution())