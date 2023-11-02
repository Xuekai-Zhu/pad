def solution():
    """Students in class 3B are collecting school points for behavior. If they get enough points in total, they can go on a trip. In the class, there are Adam, Martha, Betty, and Tom. Adam has collected 50 points. Betty was better than Adam and collected 30% more. Marta managed to collect 3 times more points than Tom, who has 30 points less than Betty. How many points is the class missing to go on the trip if the minimum threshold is 400 points?"""
    adam_points = 50
    betty_points = adam_points * 1.3
    tom_points = betty_points - 30
    marta_points = 3 * tom_points
    total_points = adam_points + betty_points + tom_points + marta_points
    points_needed = 400 - total_points
    result = points_needed
    
    return result

print(solution())