def solution():
    # Calculate the number of cookies needed for one kid to do all their chores
    cookies_needed = 3 * 4  # Patty agrees to give 3 cookies for every chore and each kid normally has 4 chores to do per week

    # Calculate the cost of one pack of cookies and the number of packs Patty can buy
    cost_per_pack = 3
    cookies_per_pack = 24
    cookies_per_dollar = cookies_per_pack / cost_per_pack
    packs_purchased = 15 / cost_per_pack

    # Calculate the number of weeks Patty can pay her siblings with cookies
    cookies_available = packs_purchased * cookies_per_pack
    weeks_without_chores = cookies_available // cookies_needed
    result = weeks_without_chores
    return result

print(solution())