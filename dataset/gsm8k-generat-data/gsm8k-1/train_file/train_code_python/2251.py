def solution():
    """Mary and Jimmy start running from the same spot, but in opposite directions. Mary runs at 5 miles per hour and Jimmy runs at 4 miles per hour. What is the distance between them after 1 hour?"""
    mary_speed = 5
    jimmy_speed = 4
    time = 1
    distance = mary_speed * time + jimmy_speed * time
    result = distance
    return result

print(solution())