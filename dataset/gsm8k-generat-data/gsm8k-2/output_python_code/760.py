def solution():
    """Joan is at the grocery store. She has a total of $60 to spend. She is going to purchase 2 containers of hummus, which are $5 each. She is going to purchase chicken for $20, bacon for $10, and vegetables for $10. She wants to purchase apples which are $2 each. With her remaining money, how many apples can she purchase?"""
    total_money = 60
    hummus_cost = 5 * 2
    chicken_cost = 20
    bacon_cost = 10
    veggie_cost = 10
    remaining_money = total_money - hummus_cost - chicken_cost - bacon_cost - veggie_cost
    apple_cost = 2
    apples_purchased = remaining_money // apple_cost
    result = apples_purchased
    return result

print(solution())