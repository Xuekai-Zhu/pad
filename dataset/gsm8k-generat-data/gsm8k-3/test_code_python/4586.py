def solution():
    """Cameron is printing her thesis in the school library and has 400 A4 pieces of paper. If 40% of the papers did not print out up to her desired quality and she separated them as invalid, calculate the total number of valid documents."""
    # Define the total number of papers and the percentage of invalid papers
    total_papers = 400
    invalid_percentage = 40

    # Calculate the number of invalid papers
    invalid_papers = (invalid_percentage / 100) * total_papers

    # Calculate the number of valid papers
    valid_papers = total_papers - invalid_papers

    # Display the total number of valid documents
    result = valid_papers
    return result

print(solution())