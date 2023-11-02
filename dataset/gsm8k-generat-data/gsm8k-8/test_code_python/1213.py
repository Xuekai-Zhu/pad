def solution():
    total_items = 75
    precious_mistakes = 12
    lyssa_mistakes = int(0.2 * total_items)  # convert decimal to integer number of mistakes
    lyssa_correct = total_items - lyssa_mistakes
    precious_correct = total_items - precious_mistakes
    difference = lyssa_correct - precious_correct
    result = difference
    return result

print(solution())