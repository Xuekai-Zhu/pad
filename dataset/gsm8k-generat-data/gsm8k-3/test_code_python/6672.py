def solution():
    """Patty decides that to convince her brother and sister to do her chores in exchange for cookies. Patty agrees to give them 3 cookies for every chore they do. Each kid normally has 4 chores to do per week. Patty has $15 to buy cookies. Each pack of cookies contains 24 cookies and costs $3. How many weeks can Patty go without doing chores by paying her siblings with cookies?"""
    # Define the number of chores and cookies per chore
    CHORES_PER_WEEK = 4
    COOKIES_PER_CHORE = 3

    # Define the cost and number of cookies per pack
    PACK_COST = 3
    COOKIES_PER_PACK = 24

    # Define the amount of money Patty has to spend on cookies
    MAX_COST = 15

    # Calculate the total number of cookies Patty can buy
    packs = MAX_COST // PACK_COST
    total_cookies = packs * COOKIES_PER_PACK

    # Calculate the total number of chores Patty can pay her siblings to do
    total_chores = total_cookies // COOKIES_PER_CHORE

    # Calculate the number of weeks Patty can go without doing chores
    weeks = total_chores // CHORES_PER_WEEK

    # Display the number of weeks
    result = weeks
    return result

print(solution())