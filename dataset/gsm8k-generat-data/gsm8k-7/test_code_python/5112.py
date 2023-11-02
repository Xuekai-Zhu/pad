def solution():
    num_paper_pieces = 5
    num_folds = 3
    num_notes_daily = 10

    # Calculate the number of small notepapers that can be made from a letter-size paper
    num_small_papers = 2 ** num_folds

    # Calculate the total number of small notepapers that can be made from the 5 letter-size papers
    total_small_papers = num_paper_pieces * num_small_papers

    # Calculate the total number of days the notepad will last
    num_days = total_small_papers // num_notes_daily
    result = num_days
    return result

print(solution())