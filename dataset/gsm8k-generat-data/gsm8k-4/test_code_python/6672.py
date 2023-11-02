def solution():
    """Patty decides that to convince her brother and sister to do her chores in exchange for cookies. Patty agrees to give them 3 cookies for every chore they do. Each kid normally has 4 chores to do per week. Patty has $15 to buy cookies. Each pack of cookies contains 24 cookies and costs $3. How many weeks can Patty go without doing chores by paying her siblings with cookies?"""
    # Define the number of chores per kid and the number of kids
    chores_per_kid = 4
    num_kids = 2

    # Define the number of cookies Patty will give for each chore done
    cookies_per_chore = 3

    # Define the budget for cookies
    budget = 15

    # Define the price and number of cookies per pack
    pack_price = 3
    cookies_per_pack = 24

    # Calculate the total number of cookies Patty can buy
    total_cookies = (budget // pack_price) * cookies_per_pack

    # Calculate the total number of chores the kids can do
    total_chores = chores_per_kid * num_kids

    # Calculate the total number of cookies needed for all the chores
    total_cookies_needed = total_chores * cookies_per_chore

    # Calculate the number of weeks Patty can go without doing chores by paying her siblings with cookies
    weeks = total_cookies // total_cookies_needed

    # Return the result
    result = weeks
    return result

print(solution())