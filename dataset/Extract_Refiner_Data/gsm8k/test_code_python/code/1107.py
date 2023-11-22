def solution():
    
    red_balls = 3
    blue_balls = 11
    green_balls = 25
    red_ball_price = 9
    blue_ball_price = 5
    green_ball_price = 3
    total_red_ball_price = red_balls * red_ball_price
    total_blue_ball_price = blue_balls * blue_ball_price
    total_green_ball_price = green_balls * green_ball_price
    total_sales = total_red_ball_price + total_blue_ball_price + total_green_ball_price
    result = total_sales
    return result

print(solution())