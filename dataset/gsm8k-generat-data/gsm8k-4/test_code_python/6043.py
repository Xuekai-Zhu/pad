def solution():
    """Carlos has some gold quarters. If he spends them in a store, they are worth the regular amount. If he melts them down, he can get $100 per ounce. Each quarter weighs 1/5 of an ounce. How many times more money would he get from melting them down instead of spending them in a store?"""
    # Define the weight and value of a single gold quarter
    weight = 1/5
    value = 0.25  # assuming the regular value of a quarter

    # Calculate the value per ounce if the quarters are melted down
    value_per_ounce = value / weight * 16 * 100

    # Calculate the ratio of the melted down value to the regular value
    ratio = value_per_ounce / value

    result = round(ratio, 2)
    return result

print(solution())