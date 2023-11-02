def solution():
    total_parents = 800
    percent_agree = 0.20

    # Calculate the number of parents who agree with the tuition fee increase
    num_agree = total_parents * percent_agree

    # Calculate the number of parents who disagree with the tuition fee increase
    num_disagree = total_parents - num_agree
    result = num_disagree
    return result

print(solution())