def solution():
    """In one of the building blocks at Oakland High there are 5 classes. Each class uses 2 whiteboards each and each whiteboard needs about 20ml of ink for a day's use. If ink costs 50 cents per ml, how much (in dollars) would it cost to use the boards for one day?"""
    # Define the number of classes and whiteboards per class
    NUM_CLASSES = 5
    WHITEBOARDS_PER_CLASS = 2

    # Define the ink required per whiteboard for a day's use
    INK_PER_WHITEBOARD = 20

    # Define the cost of ink per ml
    INK_COST_PER_ML = 0.5

    # Calculate the total ink required for one day
    total_ink = NUM_CLASSES * WHITEBOARDS_PER_CLASS * INK_PER_WHITEBOARD

    # Calculate the total cost of ink for one day
    total_cost = total_ink * INK_COST_PER_ML

    # Display the total cost
    result = total_cost
    return result

print(solution())