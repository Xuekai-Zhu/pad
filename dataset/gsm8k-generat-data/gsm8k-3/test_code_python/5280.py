def solution():
    """Haman’s father has an egg business supplying the local market. On a Wednesday morning, his father sends him to go and collect 10 trays of eggs for sale from their store. While loading the eggs into the car, he accidentally drops two trays. He calls his father telling him this, and is told to add 7 more trays for sale. How many eggs were sold that day?"""
    # Define the number of trays originally collected
    original_trays = 10

    # Define the number of trays dropped
    dropped_trays = 2

    # Define the number of trays added due to the dropped trays
    added_trays = 7

    # Calculate the total number of trays for sale
    total_trays = original_trays - dropped_trays + added_trays

    # Calculate the total number of eggs sold
    eggs_sold = total_trays * 30  # Each tray has 30 eggs

    # Display the total number of eggs sold
    result = eggs_sold
    return result

print(solution())