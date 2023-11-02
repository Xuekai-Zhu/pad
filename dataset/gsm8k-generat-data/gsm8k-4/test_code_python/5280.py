def solution():
    """Haman’s father has an egg business supplying the local market. On a Wednesday morning, his father sends him to go and collect 10 trays of eggs for sale from their store. While loading the eggs into the car, he accidentally drops two trays. He calls his father telling him this, and is told to add 7 more trays for sale. How many eggs were sold that day?"""
    # Define the number of eggs per tray
    eggs_per_tray = 30

    # Calculate the number of trays after the accident
    trays_after_accident = 10 - 2

    # Calculate the total number of trays after adding more
    total_trays = trays_after_accident + 7

    # Calculate the total number of eggs
    total_eggs = total_trays * eggs_per_tray

    # Assume that all eggs were sold
    eggs_sold = total_eggs

    result = eggs_sold
    return result

print(solution())