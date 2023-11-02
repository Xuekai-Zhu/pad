def solution():
    # Calculate the number of bolts needed for the job
    bolts_needed = 40 / 5  # for every 5 feet of pipe, one bolt is needed

    # Calculate the number of washers needed for the job
    washers_needed = bolts_needed * 2  # for every bolt, two washers are needed

    # Calculate the number of washers remaining in the bag after the job
    remaining_washers = 20 - washers_needed

    result = remaining_washers
    return result

print(solution())