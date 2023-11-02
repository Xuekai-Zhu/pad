def solution():
    """Madeline and her roommate, Keenan, share the cost of groceries. In total, they spend about $400 per month. In a four-week month, how many dollars does Keenan spend per week if Madeline pays 60% of the cost?"""
    total_cost = 400
    madeline_cost = total_cost * 0.6
    keenan_cost = total_cost - madeline_cost
    keenan_weekly_cost = keenan_cost / 4
    result = keenan_weekly_cost
    return result

print(solution())