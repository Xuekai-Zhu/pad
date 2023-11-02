def solution():
    """John writes 3 stories every week.  Each short story is 50 pages.  He also writes a novel that is 1200 pages each year.  Each sheet of paper can hold 2 pages.  Over 12 weeks, how many reams of paper does he need to buy if a ream contains 500 sheets?"""
    # Calculate the total number of pages John writes every week for short stories
    weekly_short_stories_pages = 3 * 50

    # Calculate the total number of pages John writes every year for his novel
    yearly_novel_pages = 1200

    # Calculate the total number of pages John writes over 12 weeks
    total_pages = weekly_short_stories_pages * 12 + yearly_novel_pages

    # Calculate the total number of sheets of paper John needs
    total_sheets = total_pages / 2

    # Calculate the total number of reams of paper John needs
    total_reams = total_sheets / 500

    # Display the total number of reams John needs to buy
    result = total_reams
    return result

print(solution())