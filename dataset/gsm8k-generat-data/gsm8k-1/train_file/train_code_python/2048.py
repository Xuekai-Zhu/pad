def solution():
    """Mark and his sister Chris both leave their house for school at the same time. Mark travels at the same speed as Chris, who walks 3 miles per hour. After walking 3 miles Mark has to turn around and go home because he forgot his lunch. If the distance from their house to the school is 9 miles, how much longer does Mark spend walking than Chris?"""
    chris_time = 9 / 3 # time for Chris to walk to school
    mark_time = 3 / 3 + (9 - 3) / 6 # time for Mark to walk to 3 miles and back
    difference = mark_time - chris_time # time difference between Mark and Chris
    result = difference * 60 # convert to minutes and return
    return result

print(solution())