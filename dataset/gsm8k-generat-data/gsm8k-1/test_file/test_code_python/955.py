def solution():
    """Coach brought one bag filled with basketballs to practice and dumped them all out onto the gym floor before practice began. After the practice time was over, he asked Jordan, Jason, and Jeffrey to pick up the balls and carry them over to the bag. The three boys picked up and carried all of the balls in one trip. Jordan carried twice as many balls as Jason, and Jason carried twice as many balls as Jeffrey. If Jason had picked up and carried 2 balls, what is the total number of balls that the coach brought to practice?"""
    
    jason_balls = 2
    jeffrey_balls = jason_balls / 2
    jordan_balls = jason_balls * 2
    total_balls = jason_balls + jeffrey_balls + jordan_balls
    result = total_balls
    return result

print(solution())