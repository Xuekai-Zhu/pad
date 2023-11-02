def solution():
    """Patty decides that to convince her brother and sister to do her chores in exchange for cookies. Patty agrees to give them 3 cookies for every chore they do. Each kid normally has 4 chores to do per week. Patty has $15 to buy cookies. Each pack of cookies contains 24 cookies and costs $3. How many weeks can Patty go without doing chores by paying her siblings with cookies?"""
    cookies_per_pack = 24
    cost_per_pack = 3
    packs_to_buy = 5  # $15 / $3 per pack
    chores_per_kid = 4
    cookies_per_chore = 3
    cookies_needed = packs_to_buy * cookies_per_pack
    cookies_provided_per_week = cookies_per_chore * chores_per_kid
    weeks_without_chores = cookies_needed // cookies_provided_per_week
    result = weeks_without_chores
    return result

print(solution())