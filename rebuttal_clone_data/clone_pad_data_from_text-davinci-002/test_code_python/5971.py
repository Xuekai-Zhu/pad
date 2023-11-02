def solution():
     cost_per_10_keychains = 20
     cost_per_4_keychains = 12
     number_of_keychains = 20
     packs_of_10_keychains = number_of_keychains / 10
     packs_of_4_keychains = number_of_keychains / 4
     total_cost_10_keychains = cost_per_10_keychains * packs_of_10_keychains
     total_cost_4_keychains = cost_per_4_keychains * packs_of_4_keychains
     cost_difference = total_cost_10_keychains - total_cost_4_keychains
     result = cost_difference
     return result

print(solution())