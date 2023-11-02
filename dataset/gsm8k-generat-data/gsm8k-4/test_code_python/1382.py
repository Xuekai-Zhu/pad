def solution():
    """Your video streaming subscription costs $14 a month. If you're evenly splitting the cost with your friend, how much do you pay in total after the first year for this service?"""
    # Define the subscription cost per month
    subscription_cost = 14

    # Calculate the total cost for one year
    total_cost = subscription_cost * 12

    # Calculate the cost split evenly between two friends
    split_cost = total_cost / 2

    # return the result
    result = split_cost
    return result

print(solution())