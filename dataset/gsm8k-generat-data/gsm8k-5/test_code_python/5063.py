def solution():
    pages_per_class_per_week = 2 * 5  # Chip takes 2 pages of notes per day for each of his 5 classes, for a total of 10 pages per class per week
    pages_per_week = pages_per_class_per_week * 5  # Chip has 5 classes, so he takes notes on 50 pages per week
    packs_per_week = pages_per_week / 100  # Each pack of notebook paper contains 100 sheets, so Chip uses 1/100th of a pack per page
    packs_per_6_weeks = packs_per_week * 6  # Chip wants to know how many packs of notebook paper he will use in 6 weeks

    result = packs_per_6_weeks
    return result

print(solution())