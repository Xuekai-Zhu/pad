def solution():
    """Selene buys two instant cameras at $110 and three digital photo frames at $120 each. She gets a 5% discount on all the items she purchased. How much does she pay in all?"""
    # Define the prices of each item
    CAMERA_PRICE = 110
    FRAME_PRICE = 120

    # Define the number of each item purchased
    camera_count = 2
    frame_count = 3

    # Calculate the total cost before discount
    total_cost = camera_count * CAMERA_PRICE + frame_count * FRAME_PRICE

    # Calculate the discount
    discount = total_cost * 0.05

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    # Display the total cost after discount
    result = total_cost_after_discount
    return result

print(solution())