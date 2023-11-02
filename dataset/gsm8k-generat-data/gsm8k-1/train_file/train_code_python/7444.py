def solution():
    """There were 50 people on the city bus. At the first stop, 15 people got off. At the next stop 8 people got off and 2 got on. At the third stop, 4 people got off and 3 people got on. How many people are on the bus after the third stop?"""
    starting_people = 50
    first_stop_off = 15
    second_stop_off = 8
    second_stop_on = 2
    third_stop_off = 4
    third_stop_on = 3
    
    current_people = starting_people - first_stop_off - second_stop_off + second_stop_on - third_stop_off + third_stop_on
    result = current_people
    return result

print(solution())