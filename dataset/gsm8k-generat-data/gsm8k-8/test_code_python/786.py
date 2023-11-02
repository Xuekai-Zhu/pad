def solution():
    # Calculate the total number of short story pages over 12 weeks
    short_story_pages = 3 * 50 * 12

    # Calculate the total number of novel pages in a year
    novel_pages = 1200

    # Calculate the total number of pages John needs over 12 weeks
    total_pages = short_story_pages + novel_pages / 12

    # Calculate the total number of sheets of paper needed
    total_sheets = total_pages / 2

    # Calculate the number of reams needed
    reams_needed = total_sheets / 500

    result = reams_needed
    return result

print(solution())