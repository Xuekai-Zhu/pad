def solution():
    mow_time = 40  # Max can mow the lawn in 40 minutes
    fert_time = 2 * mow_time  # It takes twice as long to fertilize the lawn as to mow it
    total_time = mow_time + fert_time  # Total time to both mow and fertilize the lawn

    result = total_time
    return result

print(solution())