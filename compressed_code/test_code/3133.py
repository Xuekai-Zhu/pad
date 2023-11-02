def solution():
    
    pop_sell_price = 1.5
    pop_make_cost = 0.9
    pencil_cost = 1.8
    pencils_needed = 100
    profit_per_pop = pop_sell_price - pop_make_cost
    pops_needed = pencils_needed * pencil_cost / profit_per_pop
    result = int(pops_needed)
    return result

print(solution())