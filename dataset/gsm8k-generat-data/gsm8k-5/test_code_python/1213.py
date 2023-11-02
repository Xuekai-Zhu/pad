def solution():
    total_items = 75  # The exam has 75 items
    lyssa_incorrect = 0.2 * total_items  # Lyssa gets 20% of the items wrong
    precious_incorrect = 12  # Precious got 12 mistakes
    lyssa_correct = total_items - lyssa_incorrect  # Lyssa got the rest of the items correct
    precious_correct = total_items - precious_incorrect  # Precious got the rest of the items correct
    
    # Calculate the difference in the number of correct answers between Lyssa and Precious
    difference = lyssa_correct - precious_correct
    result = difference
    return result

print(solution())