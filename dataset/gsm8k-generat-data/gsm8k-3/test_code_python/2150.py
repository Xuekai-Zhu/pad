def solution():
    """Rhea buys 2 trays of eggs every week for her family. Her son and daughter eat 2 eggs every morning, and Rhea and her husband eat 4 eggs every night. If each tray has 24 eggs, how many eggs are not being eaten every week?"""
    # Define the number of trays of eggs Rhea buys each week
    NUM_TRAYS = 2

    # Define the number of eggs eaten each morning by Rhea's son and daughter
    MORNING_EGGS = 4

    # Define the number of eggs eaten each night by Rhea and her husband
    NIGHT_EGGS = 8

    # Define the number of eggs in each tray
    EGGS_PER_TRAY = 24

    # Calculate the total number of eggs eaten each week
    eggs_eaten = (MORNING_EGGS * 7 * 2) + (NIGHT_EGGS * 7 * 2)

    # Calculate the total number of eggs bought each week
    eggs_bought = NUM_TRAYS * EGGS_PER_TRAY

    # Calculate the number of eggs not eaten each week
    eggs_not_eaten = eggs_bought - eggs_eaten

    # Display the number of eggs not eaten each week
    result = eggs_not_eaten
    return result

print(solution())