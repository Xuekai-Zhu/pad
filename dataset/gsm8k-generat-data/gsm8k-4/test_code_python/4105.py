def solution():
    """Andrew eats 14 donuts on Monday, and half as many on Tuesday. On Wednesday Andrew eats 4 times as many as he did on Monday. How many donuts did Andrew eat total in the three days?"""
    # Define the number of donuts Andrew eats on each day
    monday_donuts = 14
    tuesday_donuts = monday_donuts / 2
    wednesday_donuts = monday_donuts * 4

    # Calculate the total number of donuts Andrew ate
    total_donuts = monday_donuts + tuesday_donuts + wednesday_donuts
    result = total_donuts
    return result

print(solution())