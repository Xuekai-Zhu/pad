def solution():
    """A convenience store sells 180  gallons of soda a week. They buy syrup boxes that can make 30 gallons of soda, and each box costs $40. How much do they pay for syrup a week?"""
    
    # Define the amount of soda sold per week
    soda_sold = 180

    # Calculate the number of syrup boxes required per week
    syrup_boxes = soda_sold / 30

    # Calculate the total cost of syrup per week
    syrup_cost = syrup_boxes * 40

    result = syrup_cost
    return result

print(solution())