def solution():
    stories_per_week = 3
    pages_per_story = 50

    novel_pages_per_year = 1200

    pages_per_sheet = 2
    sheets_per_ream = 500

    weeks = 12

    # Calculate the total number of pages of short stories John writes in 12 weeks
    total_short_stories_pages = stories_per_week * pages_per_story * weeks

    # Calculate the total number of pages of the novel John writes in 12 weeks
    total_novel_pages = novel_pages_per_year / 12 * weeks

    # Calculate the total number of pages John writes in 12 weeks
    total_pages = total_short_stories_pages + total_novel_pages

    # Calculate the total number of sheets John needs in 12 weeks
    total_sheets = total_pages / pages_per_sheet

    # Calculate the number of reams of paper John needs to buy
    total_reams = total_sheets / sheets_per_ream
    result = total_reams
    return result

print(solution())