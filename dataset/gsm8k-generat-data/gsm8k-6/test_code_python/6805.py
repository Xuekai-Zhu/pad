def solution():
    # Calculate the total cost of iPhone 12 and iWatch after discount
    discount_iPhone = 0.15 * 800  # 15% discount on iPhone 12
    discount_iWatch = 0.1 * 300   # 10% discount on iWatch
    cost_iPhone = 800 - discount_iPhone  # cost of iPhone 12 after discount
    cost_iWatch = 300 - discount_iWatch  # cost of iWatch after discount
    total_cost = cost_iPhone + cost_iWatch  # total cost of items after discount
    cashback = 0.02 * total_cost   # 2% cashback discount
    final_cost = total_cost - cashback   # final cost after cashback

    result = final_cost
    return result

print(solution())