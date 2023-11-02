def solution():
    bill = 20
    sodas = 3
    change = 14

    # Calculate how much John paid for the sodas
    paid = bill - change

    # Calculate the cost per soda
    cost_per_soda = paid / sodas
    result = cost_per_soda
    return result

print(solution())