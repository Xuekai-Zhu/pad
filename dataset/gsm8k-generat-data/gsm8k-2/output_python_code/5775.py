def solution():
    """Tiffany is going to the beach and wants to make sure she has enough sunscreen. She knows she needs to re-apply sunscreen after 2 hours. She also knows she needs 3 ounces of sunscreen each application and a bottle contain 12 ounces and costs $3.5. If she is there for 16 hours, how much will the sunscreen cost?"""
    reapply_time = 2
    ounces_per_application = 3
    bottle_ounces = 12
    bottle_cost = 3.5
    total_sunscreen_ounces = (16 / reapply_time) * ounces_per_application
    total_bottles_needed = total_sunscreen_ounces // bottle_ounces + 1
    total_cost = bottle_cost * total_bottles_needed
    result = total_cost
    return result

print(solution())