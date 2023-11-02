def solution():
    """Carol and Jennifer are sisters from Los Angeles who love collecting signatures from celebrities. During their summer break from school, the sisters spend every afternoon collecting signatures. After five weeks, Carol and Jennifer compare their autograph books, counting up the number of signatures each sister has collected. Carol has 20 signatures in her book, and Jennifer has 44. The sisters have three more weeks of summer vacation, and they decide they want to reach 100 signatures between them by the end of the summer. How many signatures do the sisters need to collect to reach their goal?"""
    
    total_signatures_now = 20 + 44
    weeks_left = 3
    total_weeks = 5 + weeks_left
    
    signatures_per_week_needed = (100 - total_signatures_now) / weeks_left
    signatures_needed_for_goal = signatures_per_week_needed * total_weeks
    
    result = signatures_needed_for_goal
    return result

print(solution())