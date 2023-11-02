def solution():
    """Tony paid $7 for 2 dozen apples and 1 bunch of bananas. Arnold paid $5 for 1 dozen apples and 1 bunch of bananas. How much does a bunch of bananas cost?"""
    tony_cost = 7
    tony_apples = 2 * 12 # 2 dozen
    tony_bananas = 1
    arnold_cost = 5
    arnold_apples = 1 * 12 # 1 dozen
    arnold_bananas = 1
    bananas_cost = (tony_cost - arnold_cost - (tony_apples - arnold_apples) * 0.5) / tony_bananas
    result = bananas_cost
    return result

print(solution())