def solution():
    red_balls_initial = 16  # Jamie initially had 16 red balls
    blue_balls_initial = 2 * red_balls_initial  # Jamie had twice as many blue balls as red balls
    total_balls_initial = red_balls_initial + blue_balls_initial  # Jamie had this many balls initially
    red_balls_final = red_balls_initial - 6  # Jamie lost 6 of the red balls
    yellow_balls_final = 74 - (red_balls_final + blue_balls_initial)  # Jamie has 74 balls in total, so we can solve for the number of yellow balls he bought

    result = yellow_balls_final
    return result

print(solution())