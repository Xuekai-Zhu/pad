def solution():
    # Define Arnold and Hafþór's personal bests
    arnold_squat = 545
    arnold_bench = 520
    arnold_deadlift = 710
    hafthor_squat = 970
    hafthor_bench = 551
    hafthor_deadlift = 904
    # Calculate total weight lifted by both 
    arnold_total = arnold_squat + arnold_bench + arnold_deadlift
    hafthor_total = hafthor_squat + hafthor_bench + hafthor_deadlift
    # Check if Arnold's total exceeds Hafthor's
    if arnold_total > hafthor_total:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())