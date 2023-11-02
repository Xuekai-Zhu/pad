def solution():
    """Chang's Garden has two kinds of apples. Sweet ones and sour ones. He can sell the sweet ones for $.5 an apple. The sour ones sell for $.1 an apple. 75% of the apples he gets are sweet and the rest are sour. If he earns $40, how many apples did his trees give him?"""
    # Define the prices of sweet and sour apples
    SWEET_PRICE = 0.5
    SOUR_PRICE = 0.1

    # Define the percentage of apples that are sweet
    SWEET_PERCENTAGE = 0.75

    # Define the total earnings
    earnings = 40

    # Calculate the total number of apples
    total_apples = earnings / (SWEET_PRICE * SWEET_PERCENTAGE + SOUR_PRICE * (1 - SWEET_PERCENTAGE))

    # Display the total number of apples
    result = total_apples
    return result

print(solution())