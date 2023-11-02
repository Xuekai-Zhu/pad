def solution():
    total_homes = 200
    homes_distributed_first_hour = total_homes * (2/5)
    homes_remaining_first_hour = total_homes - homes_distributed_first_hour

    homes_distributed_second_hour = homes_remaining_first_hour * (60/100)
    homes_remaining_second_hour = homes_remaining_first_hour - homes_distributed_second_hour

    homes_left_overall = homes_remaining_second_hour
    result = homes_left_overall
    return result

print(solution())