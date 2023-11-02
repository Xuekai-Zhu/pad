def solution():
    # Calculate the total distance Peyton threw the ball on Saturday
    dist_Saturday = 20 * 20  # he threw the ball twenty times

    # Calculate the total distance Peyton threw the ball on Sunday
    dist_Sunday = 2 * 20 * 30  # the ball moves twice as far when the temperature is 80 degrees Fahrenheit, he threw the ball thirty times

    # Calculate the total distance Peyton threw the ball in the two days
    total_dist = dist_Saturday + dist_Sunday
    result = total_dist
    return result

print(solution())