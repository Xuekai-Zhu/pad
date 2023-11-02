def solution():
    """Cameron is printing her thesis in the school library and has 400 A4 pieces of paper.
    If 40% of the papers did not print out up to her desired quality and
    she separated them as invalid, calculate the total number of valid documents."""
    total_papers = 400
    invalid_papers = total_papers * 0.4
    valid_papers = total_papers - invalid_papers
    result = valid_papers
    return result

print(solution())