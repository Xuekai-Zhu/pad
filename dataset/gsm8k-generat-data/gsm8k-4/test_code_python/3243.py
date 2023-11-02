def solution():
    """Bella eats 6 apples a day. If during the week she consumes a third of the apples Grace picks, how many apples will Grace have after 6 weeks?"""
    # Define the number of apples Bella eats each day
    bella_daily = 6

    # Define the number of weeks for which we need to calculate the apples picked by Grace
    weeks = 6

    # Initialize the total number of apples picked by Grace
    total_grace_apples = 0

    # Calculate the number of apples picked by Grace in each week
    for i in range(1, weeks+1):
        grace_apples = (bella_daily * 7) // 3
        total_grace_apples += grace_apples

    result = total_grace_apples
    return result

print(solution())