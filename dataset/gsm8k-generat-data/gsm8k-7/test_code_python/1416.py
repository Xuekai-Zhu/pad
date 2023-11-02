def solution():
    num_employees = 5
    words_per_minute = [64, 76, 91, 80, 89]

    # Calculate the total number of words typed per minute by all employees
    total_words_per_minute = sum(words_per_minute)

    # Calculate the average number of words typed per minute by the team
    avg_words_per_minute = total_words_per_minute / num_employees
    result = avg_words_per_minute
    return result

print(solution())