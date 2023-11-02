def solution():
    """Rachel is writing an essay.  She writes 1 page every 30 minutes.  She spends 45 minutes
    researching the topic.  She writes a total of 6 pages.  Then she spends 75 minutes editing
    her essay.  Altogether, how many hours did she spend completing the essay?"""
    # Calculate the time spent writing
    writing_time = 6 * 30 # 1 page every 30 minutes

    # Calculate the total time spent on the essay
    total_time = writing_time + 45 + 75

    # Convert total time to hours
    hours = total_time / 60

    # Display the total time spent completing the essay in hours
    result = hours
    return result

print(solution())