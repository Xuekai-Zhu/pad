def solution():
    # Set up the variables
    bridge_money = 0
    sarah_money = 0

    # Loop through all possible values of Bridge's money
    for i in range(301):
        # Calculate Sarah's money based on Bridge's money
        sarah_money = 300 - i
        # If Bridge has 50 cents more than Sarah and their total is $3, return Sarah's money in cents
        if i == sarah_money + 50 and i + sarah_money == 300:
            return sarah_money
    # If no solution is found, return None
    return None

print(solution())