def solution():
    """There are currently 3 red balls, 11 blue balls, and 25 green balls in the store. Red balls cost $9, Blue balls cost $5 and green balls cost $3. How much will the store have received after all the balls are sold?"""
    num_red_balls = 3
    num_blue_balls = 11
    num_green_balls = 25
    
    red_ball_price = 9
    blue_ball_price = 5
    green_ball_price = 3
    
    total_sales = (num_red_balls * red_ball_price) + (num_blue_balls * blue_ball_price) + (num_green_balls * green_ball_price)
    
    result = total_sales
    return result

print(solution())