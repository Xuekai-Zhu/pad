def solution():
    """Ryan is looking for people to crowdfund his new business idea. If the average person funds $10 to a project they're interested in, how many people will Ryan have to recruit to fund a $1,000 business if he has $200 already?"""
    current_funds = 200
    goal_funds = 1000
    funds_needed = goal_funds - current_funds
    funding_amount = 10
    people_needed = funds_needed / funding_amount
    result = people_needed
    return result

print(solution())