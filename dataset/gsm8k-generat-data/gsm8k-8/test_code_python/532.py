def solution():
    # Convert the price to a per dozen cost
    price_per_dozen = 30 / 3

    # Calculate the total number of golf balls purchased
    dan_buys = 5 * 12
    gus_buys = 2 * 12
    chris_buys = 48

    total_balls = dan_buys + gus_buys + chris_buys

    result = total_balls
    return result

print(solution())