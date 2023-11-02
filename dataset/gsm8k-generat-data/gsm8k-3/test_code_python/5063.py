def solution():
    """Chip takes 2 pages of notes every day, 5 days a week, for each of his 5 classes.  His notebook paper comes in packs of 100 sheets of paper per pack.  After 6 weeks, how many packs of notebook paper will Chip use?"""
    # Calculate the total number of pages Chip uses in a week
    pages_per_week = 2 * 5 * 5

    # Calculate the total number of pages Chip uses in 6 weeks
    pages_per_6_weeks = pages_per_week * 6

    # Calculate the total number of packs of notebook paper Chip will need
    packs_needed = pages_per_6_weeks // 100 + 1

    # Display the total number of packs of notebook paper
    result = packs_needed

    return result

print(solution())