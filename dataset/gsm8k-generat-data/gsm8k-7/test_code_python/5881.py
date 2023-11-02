def solution():
    mpg = 30
    work_distance = 20 * 2  # 20 miles each way
    leisure_distance = 40
    num_work_days = 5

    # Calculate the total distance John drives each week
    total_distance = (work_distance * num_work_days) + leisure_distance

    # Calculate the total amount of gas John uses each week
    total_gas = total_distance / mpg

    result = total_gas
    return result

print(solution())