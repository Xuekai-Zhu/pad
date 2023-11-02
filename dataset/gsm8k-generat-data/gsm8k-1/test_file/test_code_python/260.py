def solution():
    """Carmen has $100, Samantha has $25 more than Carmen, and Daisy has $50 more than Samantha. How much do all three girls have combined?"""
    carmen_money = 100
    samantha_money = carmen_money + 25
    daisy_money = samantha_money + 50
    total_money = carmen_money + samantha_money + daisy_money
    result = total_money
    return result

print(solution())