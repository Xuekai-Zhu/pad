def solution():
    total_parents = 800  # There are 800 parents in the school
    agree_percentage = 20  # 20% of the parents agree to the tuition fee increase

    # Calculate the number of parents who agree to the tuition fee increase
    agree_parents = total_parents * agree_percentage / 100

    # Calculate the number of parents who disagree with the tuition fee increase
    disagree_parents = total_parents - agree_parents
    result = disagree_parents
    return result

print(solution())