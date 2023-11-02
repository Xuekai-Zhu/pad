def solution():
    # Calculate the number of papers delivered Monday through Saturday
    weekly_papers = 6 * 100

    # Subtract the 10 houses that don't get the Sunday paper
    sunday_papers = weekly_papers - 10

    # Add the 30 papers delivered only on Sunday
    total_papers = sunday_papers + 30
    result = total_papers
    return result

print(solution())