def solution():
    # Set up the equation for the given information
    2*1.5 + 5*x = 5.5
    # Solve for x, the cost per kilogram of salt
    x = (5.5 - 2*1.5) / 5
    # Calculate the price of 3 kilograms of sugar and 1 kilogram of salt
    price = 3*1.5 + 1*x
    result = price
    return result

print(solution())