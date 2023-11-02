def solution():
    """In one of the building blocks at Oakland High there are 5 classes.
    Each class uses 2 whiteboards each and each whiteboard needs about 20ml of ink for a day's use.
    If ink costs 50 cents per ml, how much (in dollars) would it cost to use the boards for one day?"""
    # Define the number of classes and boards used by each class
    NUM_CLASSES = 5
    BOARDS_PER_CLASS = 2

    # Define the amount of ink used by each board
    INK_PER_BOARD = 20

    # Define the cost of ink per milliliter
    INK_COST = 0.5

    # Calculate the total amount of ink used
    total_ink = NUM_CLASSES * BOARDS_PER_CLASS * INK_PER_BOARD

    # Calculate the cost of ink used
    ink_cost = total_ink * INK_COST

    # Return the result
    result = ink_cost
    return result

print(solution())