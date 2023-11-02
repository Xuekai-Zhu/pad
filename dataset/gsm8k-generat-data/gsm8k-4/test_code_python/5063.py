def solution():
    """Chip takes 2 pages of notes every day, 5 days a week, for each of his 5 classes. His notebook paper comes in packs of 100 sheets of paper per pack. After 6 weeks, how many packs of notebook paper will Chip use?"""
    # Calculate the total number of pages of notes taken per week
    weekly_notes = 2 * 5 * 5

    # Calculate the total number of pages of notes taken after 6 weeks
    total_notes = weekly_notes * 6

    # Calculate the total number of notebook paper packs needed
    paper_packs = total_notes // 100 + 1

    # Return the result
    result = paper_packs
    return result

print(solution())