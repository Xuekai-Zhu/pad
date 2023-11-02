def solution():
    
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