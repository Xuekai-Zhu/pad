def solution():
    """In one of the building blocks at Oakland High there are 5 classes. Each class uses 2 whiteboards each and each whiteboard needs about 20ml of ink for a day's use. If ink costs 50 cents per ml, how much (in dollars) would it cost to use the boards for one day?"""
    num_of_classes = 5
    num_of_boards_per_class = 2
    ink_per_board_per_day = 20
    ink_cost_per_ml = 0.5
    total_ink_needed = num_of_classes * num_of_boards_per_class * ink_per_board_per_day
    total_cost = total_ink_needed * ink_cost_per_ml
    result = total_cost
    return result

print(solution())