def solution():
     pounds = 540
     pounds_per_crate = 30
     crates = pounds / pounds_per_crate
     shipping_cost = crates * 1.5
     result = shipping_cost
     return result

print(solution())