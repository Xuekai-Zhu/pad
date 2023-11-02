def solution():
    normal_cost = 200  # Cost of a visit to a normal doctor
    discounted_cost = normal_cost * 0.3  # 70% discount on normal cost
    total_visits = 2  # Tom needs to go to the discount clinic twice
    total_normal_cost = normal_cost * total_visits  # Total cost of two visits to a normal doctor
    total_discounted_cost = discounted_cost * total_visits  # Total cost of two visits to the discount clinic
    total_saved = total_normal_cost - total_discounted_cost  # Total amount of money Tom saves
    result = total_saved
    return result

print(solution())