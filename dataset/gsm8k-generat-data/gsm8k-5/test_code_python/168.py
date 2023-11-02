def solution():
    # Calculate the total cost of the order before discount
    total_cost = (2 * 15) + (6 * 3) + (6 * 2)  # 2 quiches for $15 each, 6 croissants at $3 each, 6 biscuits at $2 each
    
    # Check if the order qualifies for the discount
    if total_cost > 50:
        # Calculate the discount
        discount = 0.1 * total_cost

        # Calculate the final cost with discount
        final_cost = total_cost - discount
    else:
        final_cost = total_cost
    
    result = final_cost
    return result

print(solution())