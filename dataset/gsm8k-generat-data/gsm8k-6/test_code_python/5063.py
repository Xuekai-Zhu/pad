def solution():
    # Calculate the total number of pages of notes Chip takes in 6 weeks
    notes_pages = 2 * 5 * 5 * 6  # Chip takes 2 pages of notes every day, 5 days a week, for each of his 5 classes, for 6 weeks
    pages_per_pack = 100  # pages per pack of notebook paper
    packs_used = (notes_pages // pages_per_pack) + 1  # add one extra pack for any remaining pages
    result = packs_used
    return result

print(solution())