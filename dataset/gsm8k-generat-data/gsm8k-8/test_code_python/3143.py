def solution():
    # Define the number of chocolate bars
    chocolate_bars = 5

    # Calculate the number of M&Ms
    mms = 7 * chocolate_bars

    # Calculate the number of marshmallows
    marshmallows = 6 * mms

    # Calculate the total number of candies
    total_candies = chocolate_bars + mms + marshmallows

    # Calculate the number of baskets
    num_baskets = total_candies // 10
    result = num_baskets
    return result

print(solution())