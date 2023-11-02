def solution():
    """On Tuesday, a fruit vendor sold 2.5 dozen lemons and 5 dozens avocados. What is the total number of fruits that the fruit vendor sold?"""
    # Define the number of fruits in a dozen
    FRUITS_PER_DOZEN = 12

    # Define the number of dozens of each type of fruit sold
    lemon_dozens = 2.5
    avocado_dozens = 5

    # Calculate the total number of lemons sold
    total_lemons = lemon_dozens * FRUITS_PER_DOZEN

    # Calculate the total number of avocados sold
    total_avocados = avocado_dozens * FRUITS_PER_DOZEN

    # Calculate the total number of fruits sold
    total_fruits = total_lemons + total_avocados

    # Display the total number of fruits sold
    result = total_fruits
    return result

print(solution())