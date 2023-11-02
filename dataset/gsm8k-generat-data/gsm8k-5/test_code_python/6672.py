def solution():
    chores_per_week = 4  # Each kid normally has 4 chores per week
    cookies_per_chore = 3  # Patty agrees to give 3 cookies for every chore done
    cookies_per_pack = 24  # Each pack of cookies contains 24 cookies
    cost_per_pack = 3  # Each pack of cookies costs $3
    budget = 15  # Patty has $15 to buy cookies

    # Calculate the total number of cookies Patty can buy
    total_cookies = (budget // cost_per_pack) * cookies_per_pack

    # Calculate the total number of chores that can be done with the cookies Patty can buy
    total_chores = total_cookies // cookies_per_chore

    # Calculate the number of weeks Patty can go without doing chores by paying her siblings with cookies
    weeks_without_chores = total_chores // chores_per_week
    result = weeks_without_chores
    return result

print(solution())