def solution():
    
    # Define the price per piece of apples picked on Monday
    monday_price = 4

    # Define the number of apples picked on Tuesday
    tuesday_picked = 12

    # Define the number of apples picked on Come Wednesday
    come_wednesday_picked = tuesday_picked * 2

    # Calculate the total number of apples picked over the three days
    total_picked = monday_price + tuesday_picked + come_wednesday_picked

    # return the result
    result = total_picked
    return result

print(solution())