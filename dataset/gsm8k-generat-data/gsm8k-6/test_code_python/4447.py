def solution():
    # Calculate the total time needed to learn the multiple-choice questions
    mc_time = 15 * 30  # 15 minutes to learn each of the 30 multiple-choice questions

    # Calculate the total time needed to learn the fill-in-the-blank questions
    fib_time = 25 * 30  # 25 minutes to learn each of the 30 fill-in-the-blank questions

    # Calculate the total time needed to study
    total_time = (mc_time + fib_time) / 60  # convert to hours
    result = total_time
    return result

print(solution())