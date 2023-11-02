def solution():
    """Adam bought 15 apples on Monday. On Tuesday he bought 3 times that quantity. On Wednesday he bought 4 times the quantity he bought on Tuesday. What is the total quantity Adam bought on these three days?"""
    # Define the quantity of apples bought on Monday
    monday_qty = 15

    # Define the quantity of apples bought on Tuesday
    tuesday_qty = monday_qty * 3

    # Define the quantity of apples bought on Wednesday
    wednesday_qty = tuesday_qty * 4

    # Calculate the total quantity of apples bought
    total_qty = monday_qty + tuesday_qty + wednesday_qty

    # Display the total quantity of apples bought
    result = total_qty
    return result

print(solution())