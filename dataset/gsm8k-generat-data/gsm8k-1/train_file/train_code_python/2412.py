def solution():
    """Val has three times as many dimes as nickels. If she accidentally finds twice as many nickels as she has in her older brother's treasure box, and takes them for herself, what would be the value of money she has, in dollars, if she had 20 nickels before finding the new ones from her brother's treasure box?"""
    nickels = 20
    dimes = 3 * nickels
    additional_nickels = 2 * nickels
    total_nickels = nickels + additional_nickels
    total_money = (nickels * 0.05) + (dimes * 0.1) + (additional_nickels * 0.05)
    result = total_money
    return result

print(solution())