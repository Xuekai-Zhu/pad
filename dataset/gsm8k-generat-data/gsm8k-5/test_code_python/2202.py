def solution():
    num_classes = 5  # There are 5 classes in one building block
    num_whiteboards_per_class = 2  # Each class uses 2 whiteboards
    ink_per_whiteboard = 20  # Each whiteboard needs 20ml of ink per day
    cost_per_ml = 0.5  # Ink costs 50 cents per ml

    # Calculate the total amount of ink used in one day
    total_ink = num_classes * num_whiteboards_per_class * ink_per_whiteboard

    # Calculate the cost of the ink used in one day
    cost_per_day = total_ink * cost_per_ml
    result = cost_per_day
    return result

print(solution())