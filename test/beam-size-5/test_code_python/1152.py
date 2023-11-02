def solution():
    
    # Define the cost of the mobile device and the selling price of the mobile device
    COST_PER_DEVICE = 20
    SELLING_PRICE_MULTIPLIER = 2

    # Define the number of devices bought last Monday and Tuesday
    num_devices_last_monday = 2
    num_devices_last_tuesday = 4

    # Calculate the total cost of the mobile devices
    total_cost = num_devices_last_monday * COST_PER_DEVICE

    # Calculate the total revenue from selling all the mobile devices
    total_revenue = num_devices_last_tuesday * SELLING_PRICE_MULTIPLIER

    # Calculate the profit from selling all the mobile devices
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())