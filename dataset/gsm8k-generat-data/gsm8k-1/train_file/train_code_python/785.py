def solution():
    """John writes 3 stories every week. Each short story is 50 pages. He also writes a novel that is 1200 pages each year. Each sheet of paper can hold 2 pages. Over 12 weeks, how many reams of paper does he need to buy if a ream contains 500 sheets?"""
    short_stories_per_week = 3
    pages_per_short_story = 50
    pages_per_novel = 1200
    sheets_per_page = 2
    total_short_story_pages_per_week = short_stories_per_week * pages_per_short_story
    total_novel_pages_per_week = pages_per_novel / 52
    total_pages_per_week = total_short_story_pages_per_week + total_novel_pages_per_week
    total_sheets_per_week = total_pages_per_week * sheets_per_page
    reams_per_week = total_sheets_per_week / 500
    reams_per_12_weeks = reams_per_week * 12
    result = reams_per_12_weeks
    return result

print(solution())