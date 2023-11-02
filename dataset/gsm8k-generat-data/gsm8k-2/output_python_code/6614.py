def solution():
    """Pete and Raymond each receive $2.50 from their grandmother. Pete saves his money and only spends 4 nickels. Raymond spends his money at the arcade games but still has 7 dimes left. How much did Pete and Raymond spent altogether, in cents?"""
    pete_money = 250
    raymond_money = 250
    pete_spent = 4 * 5  # 4 nickels
    raymond_spent = raymond_money - (7 * 10)  # 7 dimes left
    total_spent = pete_spent + raymond_spent
    result = total_spent
    return result

print(solution())