def solution():
    num_classes = 5
    num_whiteboards_per_class = 2
    ink_per_whiteboard_per_day = 20  # ml
    cost_per_ml_of_ink = 0.5  # dollars

    # Calculate the total number of whiteboards
    total_whiteboards = num_classes * num_whiteboards_per_class

    # Calculate the total amount of ink needed for one day
    total_ink_per_day = total_whiteboards * ink_per_whiteboard_per_day

    # Calculate the total cost of ink for one day
    total_cost_per_day = total_ink_per_day * cost_per_ml_of_ink
    result = total_cost_per_day
    return result

print(solution())