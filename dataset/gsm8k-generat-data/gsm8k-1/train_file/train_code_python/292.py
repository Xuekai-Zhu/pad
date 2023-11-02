def solution():
    """For every 1 minute that Carlotta sings on stage during the final opera performance, she spends an additional 3 minutes practicing and 5 minutes throwing temper tantrums. If her final stage performance is 6 minutes long, what is the total combined amount of time, in minutes, that she spends practicing, throwing tantrums, and singing in the final stage performance?"""
    singing_time = 6
    practice_time = singing_time * 3
    tantrum_time = singing_time * 5
    total_time = singing_time + practice_time + tantrum_time
    result = total_time
    return result

print(solution())