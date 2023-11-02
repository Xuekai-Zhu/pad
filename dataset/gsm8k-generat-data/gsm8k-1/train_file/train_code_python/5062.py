def solution():
    """Chip takes 2 pages of notes every day, 5 days a week, for each of his 5 classes. His notebook paper comes in packs of 100 sheets of paper per pack. After 6 weeks, how many packs of notebook paper will Chip use?"""
    pages_per_day = 2*5  # 2 pages per class, 5 classes
    days_per_week = 5
    weeks = 6
    total_pages = pages_per_day * days_per_week * weeks
    packs_of_paper = total_pages / 100
    result = packs_of_paper
    return result

print(solution())