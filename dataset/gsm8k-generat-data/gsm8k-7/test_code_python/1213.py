def solution():
    total_items = 75
    lyssa_incorrect = int(total_items * 0.2)
    precious_incorrect = 12

    # Calculate the number of correct answers for Lyssa
    lyssa_correct = total_items - lyssa_incorrect

    # Calculate the number of correct answers for Precious
    precious_correct = total_items - precious_incorrect

    # Calculate the difference between the number of correct answers of Lyssa and Precious
    difference = lyssa_correct - precious_correct
    result = difference
    return result

print(solution())