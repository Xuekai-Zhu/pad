def solution():
    """Jackson wants to go on a shopping spree, so his mom says she will give him some spending money if he does extra chores. She promises $5 per hour spent on chores.  Jackson spends 2 hours vacuuming, and decides to do this twice. He also spends 0.5 hours washing dishes, and three times as long cleaning the bathroom.  How much spending money has Jackson earned?"""
    # Define the payment per hour spent on chores
    PAYMENT_PER_HOUR = 5

    # Calculate the total time spent on chores
    total_time = (2 * 2) + 0.5 + (3 * 0.5)

    # Calculate the total amount earned
    total_earned = total_time * PAYMENT_PER_HOUR

    # Display the total amount earned
    result = total_earned
    return result

print(solution())