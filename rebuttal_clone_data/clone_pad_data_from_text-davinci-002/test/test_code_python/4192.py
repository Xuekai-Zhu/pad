def solution():
    people_on_bus_initial = 50
    people_off_first_stop = 15
    people_off_second_stop = 8
    people_on_second_stop = 2
    people_off_third_stop = 4
    people_on_third_stop = 3
    people_on_bus_final = people_on_bus_initial + people_on_second_stop - people_off_first_stop - people_off_second_stop - people_off_third_stop + people_on_third_stop
    result = people_on_bus_final
    return result

print(solution())