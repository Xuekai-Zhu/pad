def solution():
    # Calculate the rainfall on Monday and Tuesday
    rainfall_Monday = 4 + 3  # it rained 3 inches more than Sunday
    rainfall_Tuesday = 2 * rainfall_Monday  # it rained twice as much on Tuesday as Monday

    # Calculate the total rainfall over the 3 days
    total_rainfall = rainfall_Sunday + rainfall_Monday + rainfall_Tuesday
    result = total_rainfall
    return result

print(solution())