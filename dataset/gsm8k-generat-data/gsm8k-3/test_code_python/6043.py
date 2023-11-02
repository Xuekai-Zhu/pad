def solution():
    """Carlos has some gold quarters. If he spends them in a store, they are worth the regular amount. If he melts them down, he can get $100 per ounce. Each quarter weighs 1/5 of an ounce. How many times more money would he get from melting them down instead of spending them in a store?"""
    # Define the value of a gold quarter
    GOLD_QUARTER_VALUE = 0.25

    # Define the value of gold per ounce
    GOLD_VALUE_PER_OUNCE = 100

    # Define the weight of a gold quarter
    GOLD_QUARTER_WEIGHT = 1/5

    # Calculate the value of the gold quarters if spent in a store
    store_value = GOLD_QUARTER_VALUE

    # Calculate the value of the gold quarters if melted down
    melt_value = GOLD_QUARTER_WEIGHT * GOLD_VALUE_PER_OUNCE

    # Calculate how many times more money Carlos would get from melting the quarters compared to spending them in a store
    times_more_money = melt_value / store_value

    # Display the result
    result = times_more_money
    return result

print(solution())