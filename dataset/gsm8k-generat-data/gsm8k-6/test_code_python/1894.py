def solution():
    # Calculate the total hours spent on dog-walking on Monday and Wednesday
    hours_poodles_mon = 4*2
    hours_chihuahuas_mon = 2*1
    hours_labradors_wed = 4*3
    total_hours_mon_wed = hours_poodles_mon + hours_chihuahuas_mon + hours_labradors_wed

    # Calculate the total hours available for dog-walking on Tuesday
    total_hours_tue = 32 - total_hours_mon_wed

    # Calculate the number of poodles Charlotte can walk on Tuesday
    hours_chihuahuas_tue = 2*1
    hours_poodles_tue = total_hours_tue - hours_chihuahuas_tue*2
    num_poodles_tue = hours_poodles_tue//2

    result = num_poodles_tue
    return result

print(solution())