def solution():
    """Chang's Garden has two kinds of apples. Sweet ones and sour ones. He can sell the sweet ones for $.5 an apple. The sour ones sell for $.1 an apple. 75% of the apples he gets are sweet and the rest are sour. If he earns $40, how many apples did his trees give him?"""
    # Define the prices of sweet and sour apples
    sweet_price = 0.5
    sour_price = 0.1

    # Define the percentage of sweet apples
    sweet_percentage = 0.75

    # Define the total earnings
    total_earnings = 40

    # Determine the total number of apples
    total_apples = total_earnings / (sweet_price * sweet_percentage + sour_price * (1-sweet_percentage))

    result = total_apples
    return result

print(solution())