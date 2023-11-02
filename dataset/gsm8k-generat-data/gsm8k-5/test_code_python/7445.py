def solution():
    people_on_bus = 50  # There were 50 people on the bus initially
    people_off_first_stop = 15  # 15 people got off at the first stop
    people_off_second_stop = 8  # 8 people got off at the second stop
    people_on_second_stop = 2  # 2 people got on at the second stop
    people_off_third_stop = 4  # 4 people got off at the third stop
    people_on_third_stop = 3  # 3 people got on at the third stop

    # Calculate the total number of people on the bus after the third stop
    people_on_bus = people_on_bus - people_off_first_stop - people_off_second_stop - people_off_third_stop
    people_on_bus = people_on_bus + people_on_second_stop + people_on_third_stop
    result = people_on_bus
    return result

print(solution())