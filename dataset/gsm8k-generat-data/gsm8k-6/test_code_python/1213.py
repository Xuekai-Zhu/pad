def solution():
    # Calculate the number of correct answers of Lyssa
    lyssa_correct = 0.8 * 75  # Lyssa answered 20% incorrectly, so she got 80% correct

    # Calculate the number of correct answers of Precious
    precious_correct = 75 - 12  # Precious got 12 mistakes, so she got the rest of the items correct

    # Calculate the difference between the number of correct answers of Lyssa and Precious
    difference = lyssa_correct - precious_correct
    result = difference
    return result

print(solution())