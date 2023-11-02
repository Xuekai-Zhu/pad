def solution():
    # Define the starting number of listens and the number of months left in the year
    starting_listens = 60000
    months_left = 3
    
    # Calculate the total number of listens using a loop that doubles the number of listens each month
    total_listens = starting_listens
    for i in range(months_left):
        total_listens *= 2
    
    result = total_listens
    return result

print(solution())