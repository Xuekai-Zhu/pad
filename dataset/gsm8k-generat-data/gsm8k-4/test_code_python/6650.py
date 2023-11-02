def solution():
    """Danivan Drugstore has 4500 bottles of hand sanitizer gel in inventory at the beginning of the week. On Monday 2445 bottles were sold, on Tuesday 900 bottles were sold, and 50 bottles each day for the rest of the week were sold (from Wednesday until Sunday). On Saturday, the supplier delivers an order for 650 bottles. How many bottles of sanitizer gel does the Drugstore have at the end of the week?"""
    # Define the initial number of sanitizer bottles
    sanitizer_bottles = 4500

    # Calculate the number of sanitizer bottles sold from Monday to Tuesday
    sold_bottles = 2445 + 900

    # Calculate the number of sanitizer bottles sold from Wednesday to Sunday
    sold_bottles += (50 * 5)

    # Subtract the sold bottles from the initial inventory
    sanitizer_bottles -= sold_bottles

    # Add the supplier's delivery
    sanitizer_bottles += 650

    # return the result
    result = sanitizer_bottles
    return result

print(solution())