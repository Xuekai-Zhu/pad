def solution():
    # convert all time units to minutes
    proof_time = 2 * 60
    bake_time = 30
    cool_time = 15
    total_prep_time = 60 + 15 + proof_time + bake_time + cool_time

    # calculate the latest start time by subtracting prep time from the store's opening time
    opening_time = 6 * 60  # 6:00am = 360 minutes
    latest_start_time = opening_time - total_prep_time
    result = latest_start_time
    return result

print(solution())