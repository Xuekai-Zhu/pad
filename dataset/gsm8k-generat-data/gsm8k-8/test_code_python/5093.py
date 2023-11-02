def solution():
    # Let x be the number of times Maurice had ridden before his visit
    x = 0

    # Calculate the total number of times Matt rode during the two weeks
    total_rides = 8 + 16 + (3*x)

    # Solve for x using the equation above
    x = (total_rides - 24) / 3
    
    result = x
    return result

print(solution())