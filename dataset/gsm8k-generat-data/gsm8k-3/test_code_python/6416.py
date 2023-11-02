def solution():
    """Frank is practicing a new dance move.  It starts with him take 5 steps back, and then 10 steps forward, and then 2 steps back, and then double that amount forward.  How many steps forward is Frank from his original starting point?"""
    # Frank's initial position is 0
    position = 0

    # Frank takes 5 steps back
    position -= 5

    # Frank takes 10 steps forward
    position += 10

    # Frank takes 2 steps back
    position -= 2

    # Frank takes double the previous amount forward, which is 2*2=4 steps
    position += 4

    # Frank's final position
    result = position
    return result

print(solution())