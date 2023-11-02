def solution():
    """Janet buys a multi-flavor pack of cheese sticks. 15 of the sticks are cheddar, 30 are mozzarella, and 45 are pepperjack. If Janet picks a cheese stick at random, what is the percentage chance it will be pepperjack?"""
    total_sticks = 15 + 30 + 45
    pepperjack_sticks = 45
    percentage = (pepperjack_sticks/total_sticks) * 100
    result = percentage
    return result

print(solution())