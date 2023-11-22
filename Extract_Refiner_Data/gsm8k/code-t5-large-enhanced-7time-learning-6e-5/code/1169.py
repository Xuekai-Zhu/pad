def solution():
    
    # Define the regular price of the dishwasher pods
    REGULAR_PRICE = 12

    # Define the number of dishwasher pods in the regular box
    REGULAR_PODS = 100

    # Calculate the price of the new box with 20% more pods
    new_box_price = REGULAR_PRICE * 1.2

    # Calculate the number of dishwashing cycles that can be run with the new box
    cycles = (REGULAR_PODS // new_box_price) // 1

    # Display the number of dishwashing cycles
    result = cycles
    return result

print(solution())