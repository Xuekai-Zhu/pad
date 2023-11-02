def solution():
    """Patty decides that to convince her brother and sister to do her chores in exchange for cookies. Patty agrees to give them 3 cookies for every chore they do. Each kid normally has 4 chores to do per week. Patty has $15 to buy cookies. Each pack of cookies contains 24 cookies and costs $3. How many weeks can Patty go without doing chores by paying her siblings with cookies?"""
    cookies_per_pack = 24
    pack_price = 3
    total_budget = 15
    cookies_per_chore = 3
    chores_per_week = 4
    cookies_per_week = cookies_per_chore * chores_per_week
    total_cookies_needed = cookies_per_week * 2  # for two siblings
    packs_needed = total_cookies_needed / cookies_per_pack
    total_price = packs_needed * pack_price
    weeks_without_chores = total_budget // total_price
    result = weeks_without_chores
    return result

print(solution())