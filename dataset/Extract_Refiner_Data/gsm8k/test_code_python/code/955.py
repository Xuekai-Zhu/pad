def solution():
    
    # Define the number of balls picked up by Jason and carried by Jeffrey
    jason_balls = 2
    jeffrey_balls = 2

    # Calculate the number of balls carried by Jordan and Jason
    jordan_balls = jason_balls * 2
    jason_carried_balls = jeffrey_balls * 2

    # Calculate the total number of balls picked up and carried by all three boys
    total_balls = jason_balls + jeffrey_balls + jordan_balls + jason_carried_balls

    # Display the total number of balls picked up and carried
    result = total_balls
    return result

print(solution())