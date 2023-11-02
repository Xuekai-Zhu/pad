def solution():
     brownies_baked = 2
     brownies_eaten = 1 + (0.75 * 2)
     ice_cream_scoops = 8
     scoops_eaten = brownies_eaten * 2
     tubs_used = scoops_eaten / ice_cream_scoops
     result = tubs_used
     return result

print(solution())