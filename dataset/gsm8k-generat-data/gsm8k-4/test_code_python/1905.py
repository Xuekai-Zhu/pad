def solution():
    """Edward the plumber is replacing a pipe in a bathroom wall. He needs to use 40 feet of copper pipe to complete the job. For every 5 feet of pipe, Edward must use one tightening bolt, and for every bolt, he uses two washers. He buys a bag of 20 washers for the job. After he completes the bathroom job, how many washers will be remaining in the bag?"""
    # Calculate the number of bolts needed
    bolts = 40 // 5  # double line used to round down to the nearest integer

    # Calculate the number of washers needed
    washers = bolts * 2

    # Calculate the number of washers remaining in the bag after the job
    remaining_washers = 20 - washers

    result = remaining_washers
    return result

print(solution())