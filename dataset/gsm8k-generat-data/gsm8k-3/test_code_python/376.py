def solution():
    """There are 40 more buyers in the grocery store today than yesterday. There were half the number of buyers yesterday as there were the day before, and the day before had 50 buyers. Nobody visited the store on more than one day. What's the total number of buyers who've visited the store in the three days?"""
    # Define the number of buyers on each day
    day_before_yesterday = 50
    yesterday = day_before_yesterday / 2
    today = yesterday + 40

    # Calculate the total number of buyers over the three days
    total_buyers = day_before_yesterday + yesterday + today

    # Display the total number of buyers
    result = total_buyers
    return result

print(solution())