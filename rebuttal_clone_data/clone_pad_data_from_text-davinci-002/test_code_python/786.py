def solution():
    stories_per_week= 3
    pages_per_story = 50
    novels_per_year = 1
    pages_per_novel = 1200
    pages_per_sheet = 2
    sheets_per_ream = 500
    total_pages = (stories_per_week * pages_per_story * 12) + (novels_per_year * pages_per_novel)
    total_sheets = total_pages / pages_per_sheet
    total_reams = total_sheets / sheets_per_ream
    result = total_reams
    return result

print(solution())