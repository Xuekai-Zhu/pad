def solution():
    """On Monday, Sydney sends 5 texts each to Allison and Brittney. On Tuesday, she sends 15 texts to each of them. In total, how many texts did Sydney send to Allison and Brittney on both days?"""
    # Calculate the total number of texts sent on Monday
    monday_texts = 5 * 2

    # Calculate the total number of texts sent on Tuesday
    tuesday_texts = 15 * 2

    # Calculate the total number of texts sent on both days
    total_texts = monday_texts + tuesday_texts

    # return the result
    result = total_texts
    return result

print(solution())