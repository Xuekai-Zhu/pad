def solution():
    """A convenience store sells 180 gallons of soda a week. They buy syrup boxes that can make 30 gallons of soda, and each box costs $40. How much do they pay for syrup a week?"""
    # Define the number of gallons of soda the store sells per week
    soda_gallons_per_week = 180

    # Define the number of gallons of soda each syrup box can make
    syrup_gallons_per_box = 30

    # Define the cost of each syrup box
    syrup_cost_per_box = 40

    # Calculate the number of syrup boxes needed per week
    syrup_boxes_per_week = soda_gallons_per_week / syrup_gallons_per_box

    # Calculate the total cost of syrup per week
    syrup_cost_per_week = syrup_boxes_per_week * syrup_cost_per_box

    # Display the cost of syrup per week
    result = syrup_cost_per_week
    return result

print(solution())