def solution():
    """Danivan Drugstore has 4500 bottles of hand sanitizer gel in inventory at the beginning of the week. On Monday 2445 bottles were sold, on Tuesday 900 bottles were sold, and 50 bottles each day for the rest of the week were sold (from Wednesday until Sunday). On Saturday, the supplier delivers an order for 650 bottles. How many bottles of sanitizer gel does the Drugstore have at the end of the week?"""
    # Define the initial inventory
    initial_inventory = 4500

    # Calculate the total number of bottles sold from Monday to Sunday
    total_sold = 2445 + 900 + 50*5

    # Calculate the total number of bottles received on Saturday
    total_received = 650

    # Calculate the final inventory
    final_inventory = initial_inventory - total_sold + total_received

    # Display the final inventory
    result = final_inventory
    return result

print(solution())