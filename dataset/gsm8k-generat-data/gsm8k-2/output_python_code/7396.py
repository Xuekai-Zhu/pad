def solution():
    """Ryan is looking for people to crowdfund his new business idea. If the average person funds $10 to a project they're interested in, how many people will Ryan have to recruit to fund a $1,000 business if he has $200 already?"""
    current_funds = 200
    target_funds = 1000
    avg_fund_per_person = 10
    total_funds_needed = target_funds - current_funds
    num_people_needed = total_funds_needed / avg_fund_per_person
    result = num_people_needed
    return result

print(solution())