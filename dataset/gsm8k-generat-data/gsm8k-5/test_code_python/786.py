def solution():
    stories_per_week = 3  # John writes 3 short stories every week
    pages_per_story = 50  # Each short story is 50 pages
    total_pages_stories = stories_per_week * pages_per_story * 12  # John writes stories for 12 weeks
    pages_per_novel = 1200  # John writes a novel that is 1200 pages each year
    total_pages_novel = pages_per_novel / 52 * 12  # John writes the novel over 12 weeks
    total_pages = total_pages_stories + total_pages_novel  # John writes both short stories and a novel

    pages_per_ream = 500  # A ream contains 500 sheets of paper
    pages_per_sheet = 2  # Each sheet of paper holds 2 pages
    total_sheets = total_pages / pages_per_sheet  # Calculate the total number of sheets needed
    total_reams = total_sheets / pages_per_ream  # Calculate the total number of reams needed
    result = total_reams
    return result

print(solution())