def solution():
    """Josh decides to take up juggling to perform at the school talent show a month in the future. He starts off practicing juggling 3 balls, and slowly gets better adding 1 ball to his juggling act each week. After the end of the fourth week the talent show begins, but when Josh walks on stage he slips and drops three of his balls. 2 of them are caught by people in the crowd as they roll off the stage, but one gets lost completely since the auditorium is dark. With a sigh, Josh starts to juggle on stage with how many balls?"""
    starting_balls = 3
    balls_added = 1
    weeks_practicing = 4
    current_balls = starting_balls + (balls_added * weeks_practicing)
    balls_lost = 1
    balls_caught = 2
    final_balls = current_balls - balls_lost + balls_caught
    result = final_balls
    return result

print(solution())