def solution():
    """Jenny's property tax rate is 2%. Her house is currently worth $400,000. The city is about to build a new high-speed rail project nearby, which will increase her house's value by 25%. Jenny can only afford to spend $15,000/year on property tax. How many dollars worth of improvements can she make to her house before her property tax bill gets too high?"""
    # Define the initial parameters
    TAX_RATE = 0.02
    INITIAL_VALUE = 400000
    MAX_TAX = 15000

    # Calculate the new value of the house with the high-speed rail improvement
    improved_value = INITIAL_VALUE * 1.25

    # Calculate the maximum allowable value after property taxes
    max_value = (MAX_TAX / TAX_RATE)

    # Calculate the maximum improvement value
    improvement_value = max_value - INITIAL_VALUE

    # Display the maximum improvement value
    result = improvement_value
    return result

print(solution())