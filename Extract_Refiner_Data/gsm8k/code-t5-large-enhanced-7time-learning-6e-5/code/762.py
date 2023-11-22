def solution():
    
    # Define the cost of the ball and the initial amount of money
    ball_cost = 20
    initial_money = 80

    # Calculate the amount of money left after buying the ball
    remaining_money = initial_money - ball_cost

    # Calculate the number of candy bars Marissa bought for Jimmy
    candy_bars = remaining_money // 5

    # return the result
    result = candy_bars
    return result

print(solution())