def solution():
    """Adam bought 15 apples on Monday. On Tuesday he bought 3 times that quantity. On Wednesday he bought 4 times the quantity he bought on Tuesday. What is the total quantity Adam bought on these three days?"""
    # Define the quantity of apples Adam bought on Monday
    monday_quantity = 15

    # Calculate the quantity of apples Adam bought on Tuesday
    tuesday_quantity = monday_quantity * 3

    # Calculate the quantity of apples Adam bought on Wednesday
    wednesday_quantity = tuesday_quantity * 4

    # Calculate the total quantity of apples Adam bought
    total_quantity = monday_quantity + tuesday_quantity + wednesday_quantity

    # return the result
    result = total_quantity
    return result

print(solution())