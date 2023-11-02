def solution():
    total_papers = 400  # Cameron has 400 pieces of paper
    invalid_papers = 0.4 * total_papers  # 40% of the papers are invalid

    # Calculate the total number of valid papers
    valid_papers = total_papers - invalid_papers
    result = valid_papers
    return result

print(solution())