def solution():
    # Define the number of questions answered and the percentage correct for each section
    questions1 = 40
    percent_correct1 = 0.9
    questions2 = 40
    percent_correct2 = 0.95

    # Calculate the total number of questions answered correctly
    correct1 = questions1 * percent_correct1
    correct2 = questions2 * percent_correct2
    total_correct = correct1 + correct2
    result = total_correct
    return result

print(solution())