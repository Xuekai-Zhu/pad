def solution():
    """Melanie's father opens up an animal farm starting with 50 cows and 20 chickens. Milkie Cows Limited brings him 20 cows per day and Broilers Limited brings him 10 chickens per day, for three weeks. What's the total number of animals on the farm after three weeks?"""
    initial_cows = 50
    initial_chickens = 20
    cows_per_day = 20
    chickens_per_day = 10
    days = 21 # three weeks

    total_cows = initial_cows + (cows_per_day * days)
    total_chickens = initial_chickens + (chickens_per_day * days)
    result = total_cows + total_chickens

    return result

print(solution())