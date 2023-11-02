def solution():
    num_passes_thrown = 80
    no_throw_percent = 0.3
    no_throw_sack_percent = 0.5

    # Calculate the number of times the quarterback does not throw the ball
    num_no_throw = num_passes_thrown * no_throw_percent

    # Calculate the number of times the quarterback is sacked when not throwing the ball
    num_no_throw_sacked = num_no_throw * no_throw_sack_percent

    result = num_no_throw_sacked
    return result

print(solution())