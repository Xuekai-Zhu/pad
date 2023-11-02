def solution():
    """Haman’s father has an egg business supplying the local market. On a Wednesday morning, his father sends him to go and collect 10 trays of eggs for sale from their store. While loading the eggs into the car, he accidentally drops two trays. He calls his father telling him this, and is told to add 7 more trays for sale. How many eggs were sold that day?"""
    initial_trays = 10
    dropped_trays = 2
    added_trays = 7
    total_trays = initial_trays - dropped_trays + added_trays
    eggs_per_tray = 30
    total_eggs = total_trays * eggs_per_tray
    result = total_eggs
    return result

print(solution())