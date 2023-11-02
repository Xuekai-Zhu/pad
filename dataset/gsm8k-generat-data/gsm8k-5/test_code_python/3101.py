def solution():
    soda_per_week = 180  # The store sells 180 gallons of soda a week
    soda_per_box = 30  # Each box of syrup makes 30 gallons of soda
    cost_per_box = 40  # Each box costs $40

    # Calculate the number of boxes required per week
    boxes_per_week = soda_per_week / soda_per_box

    # Calculate the total cost of syrup per week
    cost_per_week = boxes_per_week * cost_per_box
    result = cost_per_week
    return result

print(solution())