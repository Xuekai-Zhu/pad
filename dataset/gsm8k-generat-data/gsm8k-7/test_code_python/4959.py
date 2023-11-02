def solution():
    num_mcq_written = 35 * 2 / 5  # 2/5 of 35 multiple-choice questions
    num_ps_written = 15 * 1 / 3  # 1/3 of 15 problem-solving questions

    # Calculate the remaining number of multiple-choice and problem-solving questions
    remaining_mcq = 35 - num_mcq_written
    remaining_ps = 15 - num_ps_written

    # Calculate the total number of questions that Meryll needs to write
    total_remaining = remaining_mcq + remaining_ps
    result = total_remaining
    return result

print(solution())