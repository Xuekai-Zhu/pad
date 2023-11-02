def solution():
    """A trolley driver picked up 10 people on his 1st stop. On the next stop, 3 people got off and twice as many people from the 1st stop got on. On the third stop, 18 people got off and 2 got on. How many people are currently on the trolley?"""
    passengers = 10
    passengers -= 3
    passengers += 2*10
    passengers -= 18
    passengers += 2
    result = passengers
    return result

print(solution())