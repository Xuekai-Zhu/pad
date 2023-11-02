def solution():
    golf_balls_per_dozen = 12  # 1 dozen contains 12 golf balls
    price_for_3_dozen = 30  # A price of $30 is charged for 3 dozen golf balls
    dan_buys = 5 * golf_balls_per_dozen  # Convert 5 dozen to number of golf balls
    gus_buys = 2 * golf_balls_per_dozen  # Convert 2 dozen to number of golf balls
    chris_buys = 48  # Chris buys directly in terms of number of golf balls

    # Calculate the total number of golf balls purchased
    total_golf_balls = dan_buys + gus_buys + chris_buys
    result = total_golf_balls
    return result

print(solution())