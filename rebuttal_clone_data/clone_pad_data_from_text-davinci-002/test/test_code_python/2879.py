def solution():
    nose_piercing_cost = 20
    ears_piercing_cost = nose_piercing_cost * 1.5
    total_nose_piercings = 6
    total_ears_piercings = 9
    total_revenue = (total_nose_piercings * nose_piercing_cost) + (total_ears_piercings * ears_piercing_cost)
    result = total_revenue
    return result

print(solution())