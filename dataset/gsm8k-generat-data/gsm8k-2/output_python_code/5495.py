def solution():
    """A trolley driver picked up 10 people on his 1st stop. On the next stop, 3 people got off and twice as many people from the 1st stop got on. On the third stop, 18 people got off and 2 got on. How many people are currently on the trolley?"""
    first_stop = 10
    second_stop = first_stop * 2 - 3
    third_stop = second_stop - 18 + 2
    total_people = third_stop
    result = total_people
    return result

print(solution())