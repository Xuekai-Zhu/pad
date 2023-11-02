def solution():
    """Edward the plumber is replacing a pipe in a bathroom wall.  He needs to use 40 feet of copper pipe to complete the job.  For every 5 feet of pipe, Edward must use one tightening bolt, and for every bolt, he uses two washers.  He buys a bag of 20 washers for the job.  After he completes the bathroom job, how many washers will be remaining in the bag?"""
    # Define the amount of pipe needed and the number of bolts and washers required
    PIPE_LENGTH = 40
    BOLTS_PER_PIPE = 1/5
    WASHERS_PER_BOLT = 2

    # Calculate the number of bolts needed
    bolts_needed = PIPE_LENGTH * BOLTS_PER_PIPE

    # Calculate the total number of washers needed
    washers_needed = bolts_needed * WASHERS_PER_BOLT

    # Calculate the number of washers remaining in the bag
    washers_remaining = 20 - washers_needed

    # Display the number of washers remaining
    result = washers_remaining
    return result

print(solution())