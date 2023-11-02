def solution():
    """Socorro is preparing for a math contest. She needs to train for a total of 5 hours. Each day, she answers problems about multiplication for 10 minutes and then division problems for 20 minutes. How many days will it take for her to complete her training?"""
    # Define the time for each set of problems
    MUL_TIME = 10  # minutes
    DIV_TIME = 20  # minutes

    # Define the total time for training
    TOTAL_TIME = 5 * 60  # minutes

    # Calculate the time for each pair of problems
    pair_time = MUL_TIME + DIV_TIME

    # Calculate the number of pairs of problems Socorro can do within the total training time
    pairs_total = TOTAL_TIME // pair_time

    # Calculate the number of days needed for training
    days_total = pairs_total // 2  # since there are 2 pairs per day

    # Display the number of days needed for training
    result = days_total
    return result

print(solution())