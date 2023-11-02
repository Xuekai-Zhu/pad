def solution():
    """Tiffany is going to the beach and wants to make sure she has enough sunscreen. She knows she needs to re-apply sunscreen after 2 hours. She also knows she needs 3 ounces of sunscreen each application and a bottle contains 12 ounces and costs $3.5. If she is there for 16 hours, how much will the sunscreen cost?"""
    hours_per_application = 2
    ounces_per_application = 3
    ounces_per_bottle = 12
    cost_per_bottle = 3.5
    
    num_applications = 16 // hours_per_application
    num_bottles = (num_applications * ounces_per_application) / ounces_per_bottle
    total_cost = num_bottles * cost_per_bottle
    
    result = total_cost
    return result

print(solution())