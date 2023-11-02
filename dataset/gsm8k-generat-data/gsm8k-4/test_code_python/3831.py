def solution():
    """Jerry bought 48 firecrackers for the 4th of July. A police officer discovered and confiscated 12 of them. 1/6 of the remaining ones were defective. If Jerry set off half the good firecrackers, how many firecrackers did he set off?"""
    # Define the initial number of firecrackers
    initial_firecrackers = 48

    # Define the number of firecrackers confiscated by the police officer
    confiscated_firecrackers = 12

    # Calculate the number of remaining firecrackers
    remaining_firecrackers = initial_firecrackers - confiscated_firecrackers

    # Calculate the number of defective firecrackers
    defective_firecrackers = remaining_firecrackers / 6

    # Calculate the number of good firecrackers
    good_firecrackers = remaining_firecrackers - defective_firecrackers

    # Calculate the number of firecrackers set off by Jerry
    jerry_firecrackers = good_firecrackers / 2

    # Return the result
    result = jerry_firecrackers
    return result

print(solution())