def solution():
    hair_cost = 50  # Cost of hair updo
    manicure_cost = 30  # Cost of manicure
    tip_percent = 0.2  # 20% tip for each beautician
    total_cost = (hair_cost + manicure_cost) * (1 + tip_percent)  # Total cost with tip

    result = total_cost
    return result

print(solution())