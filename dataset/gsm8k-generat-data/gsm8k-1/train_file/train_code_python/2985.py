def solution():
    """Miley bought two cellphones for her parents. Each cellphone costs $800 but, since she is buying two units, she will receive a 5% discount for the total cost. How much did Miley pay?"""
    cellphone_cost = 800
    num_cellphones = 2
    total_cost = cellphone_cost * num_cellphones
    discount = 5
    discounted_amount = (discount / 100) * total_cost
    final_cost = total_cost - discounted_amount
    result = final_cost
    return result

print(solution())