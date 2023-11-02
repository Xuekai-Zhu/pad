def solution():
    """Edward the plumber is replacing a pipe in a bathroom wall. He needs to use 40 feet of copper pipe to complete the job. For every 5 feet of pipe, Edward must use one tightening bolt, and for every bolt, he uses two washers. He buys a bag of 20 washers for the job. After he completes the bathroom job, how many washers will be remaining in the bag?"""
    pipe_length = 40
    bolts_needed = pipe_length // 5
    washers_needed = bolts_needed * 2
    washers_remaining = 20 - washers_needed
    result = washers_remaining
    return result

print(solution())