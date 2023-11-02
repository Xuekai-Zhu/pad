def solution():
    # Calculate the total cost of the living room set
    total_cost = 2500 + 3500 + 2000  # coach + sectional + everything else
    discount = total_cost * 0.10  # 10% discount on everything
    final_cost = total_cost - discount  # final cost after discount
    result = final_cost
    return result

print(solution())