def solution():
    # Calculate the points Jaron has so far
    current_points = 8 * 100  # he sold 8 chocolate bunnies that are worth 100 points each

    # Calculate the number of Snickers bars he needs to sell to reach 2000 points
    snickers_needed = (2000 - current_points) / 25

    result = snickers_needed
    return result

print(solution())