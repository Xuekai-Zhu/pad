def solution():
    # Calculate the total number of papers delivered from Monday to Saturday
    papers_mon_to_sat = 100 * 6  # Kyle delivers to 100 houses for 6 days

    # Calculate the total number of papers delivered on Sunday
    papers_sunday = (100 - 10) + 30  # Kyle delivers to 100-10=90 houses and 30 extra papers

    # Calculate the total number of papers delivered in a week
    total_papers = papers_mon_to_sat + papers_sunday
    result = total_papers
    return result

print(solution())