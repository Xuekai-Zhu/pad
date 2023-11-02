def solution():
    """John writes 3 stories every week. Each short story is 50 pages. He also writes a novel that is 1200 pages each year. Each sheet of paper can hold 2 pages. Over 12 weeks, how many reams of paper does he need to buy if a ream contains 500 sheets?"""
    short_story_pages = 50
    weekly_short_stories = 3
    yearly_novel_pages = 1200
    paper_capacity = 2
    total_short_story_pages = short_story_pages * weekly_short_stories * 12
    total_novel_pages = yearly_novel_pages
    total_paper_pages = total_short_story_pages + total_novel_pages
    total_paper_sheets = total_paper_pages / paper_capacity
    reams_needed = round(total_paper_sheets / 500)
    result = reams_needed
    return result

print(solution())