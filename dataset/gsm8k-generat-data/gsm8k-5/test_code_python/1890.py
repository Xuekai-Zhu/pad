def solution():
    # Calculate the number of towels each person can fold in 1 minute
    rate_jane = 3/5 
    rate_kyla = 5/10 
    rate_anthony = 7/20 

    # Calculate the total number of towels they can fold in 1 minute
    total_rate = rate_jane + rate_kyla + rate_anthony 

    # Calculate the total number of towels they can fold in 1 hour (60 minutes)
    towels_per_hour = total_rate * 60 

    result = towels_per_hour
    return result

print(solution())