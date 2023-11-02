def solution():
    """Some people got on a bus at the terminal. At the first bus stop, 5 more people got in. Then at the second bus stop, 7 people got down and 8 more got in. If there were a total of 20 people heading to the third stop, how many people got on the bus at the terminal?"""
    total_people_at_third_stop = 20
    people_down_at_second_stop = 7
    people_at_second_stop = people_down_at_second_stop + 8
    people_at_first_stop = people_at_second_stop - 5
    people_at_terminal = total_people_at_third_stop - people_at_second_stop
    result = people_at_terminal
    return result

print(solution())