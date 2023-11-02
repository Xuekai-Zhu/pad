def solution():
    """Ursula bought five hot dogs at $1.50 each and three salads at $2.50 each. If she had two $10 bills, how much change did she get back?"""
    hot_dog_cost = 1.5
    salad_cost = 2.5
    num_hot_dogs = 5
    num_salads = 3
    total_cost = (hot_dog_cost * num_hot_dogs) + (salad_cost * num_salads)
    paid_with = 10 * 2
    change = paid_with - total_cost
    result = change
    
    return result

print(solution())