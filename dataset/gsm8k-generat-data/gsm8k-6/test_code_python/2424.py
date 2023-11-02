def solution():
    # Calculate Jen and Sammy's scores
    jen_score = 20 + 10  # Jen scored 10 more than Bryan
    sammy_score = jen_score - 2  # Sammy scored 2 fewer than Jen

    # Calculate the total number of points missed on the exam
    total_missed = 35 - (20 + jen_score + sammy_score)

    result = total_missed
    return result

print(solution())