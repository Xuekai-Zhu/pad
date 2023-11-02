def solution():
    price_for_3_dozen = 30
    num_golf_balls_per_dozen = 12

    dan_buy = 5
    gus_buy = 2
    chris_buy = 48 / num_golf_balls_per_dozen

    # Calculate the total number of golf balls purchased
    total_golf_balls = dan_buy * num_golf_balls_per_dozen + gus_buy * num_golf_balls_per_dozen + chris_buy

    result = total_golf_balls
    return result

print(solution())