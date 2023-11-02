def solution():
    num_red_balls = 3
    red_ball_price = 9

    num_blue_balls = 11
    blue_ball_price = 5

    num_green_balls = 25
    green_ball_price = 3

    # Calculate the total revenue from all red balls
    total_red_revenue = num_red_balls * red_ball_price

    # Calculate the total revenue from all blue balls
    total_blue_revenue = num_blue_balls * blue_ball_price

    # Calculate the total revenue from all green balls
    total_green_revenue = num_green_balls * green_ball_price

    # Calculate the total revenue from all balls
    total_revenue = total_red_revenue + total_blue_revenue + total_green_revenue
    result = total_revenue
    return result

print(solution())