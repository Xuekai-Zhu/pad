def solution():
    """Jerry was contracted to work on a house by his neighbor Miss Stevie. The time it took him to fix the broken kitchen counter was three times longer than the time he took painting the house. He took 8 hours painting the house and then helped mow Miss Stevie's lawn, taking 6 hours. If he charged Miss Stevie $15 per hour of work, calculate the amount of money that Miss Stevie paid him."""
    painting_time = 8
    counter_fixing_time = 3 * painting_time
    lawn_mowing_time = 6
    total_time = painting_time + counter_fixing_time + lawn_mowing_time
    hourly_rate = 15
    total_payment = total_time * hourly_rate
    result = total_payment
    return result

print(solution())