def solution():
    # Calculate the total cost of the 6 t-shirts
    initial_cost = 6 * 20  # each shirt costs $20
    discount = 50/100  # 50% discount
    final_cost = initial_cost * (1-discount)  # cost after discount
    result = final_cost
    return result

print(solution())