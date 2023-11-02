def solution():
    # Calculate the total number of short story pages John writes in 12 weeks
    short_story_pages = 3 * 50 * 12

    # Calculate the total number of novel pages John writes in 12 weeks
    novel_pages = 1200 / 52 * 12

    # Calculate the total number of pages John writes in 12 weeks
    total_pages = short_story_pages + novel_pages

    # Calculate the total number of sheets of paper John needs
    total_sheets = total_pages / 2

    # Calculate the total number of reams of paper John needs to buy
    total_reams = total_sheets / 500
    result = total_reams
    return result

print(solution())