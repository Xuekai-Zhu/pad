def solution():
    """John writes 3 stories every week. Each short story is 50 pages. He also writes a novel that is 1200 pages each year. Each sheet of paper can hold 2 pages. Over 12 weeks, how many reams of paper does he need to buy if a ream contains 500 sheets?"""
    # Define the number of short stories and the number of pages per story
    num_stories = 3
    story_pages = 50

    # Calculate the total number of short story pages written over 12 weeks
    total_story_pages = num_stories * story_pages * 12

    # Calculate the number of novel pages written over 12 weeks
    novel_pages = 1200

    # Calculate the total number of pages written over 12 weeks
    total_pages = total_story_pages + novel_pages

    # Calculate the number of sheets of paper needed
    num_sheets = total_pages / 2

    # Calculate the number of reams of paper needed
    num_reams = num_sheets / 500

    result = round(num_reams)
    return result

print(solution())