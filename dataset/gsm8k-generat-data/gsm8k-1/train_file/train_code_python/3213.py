def solution():
    """Carla had 400 chickens on her chicken farm. However, 40% of the chicken died due to a certain disease. How many chickens were there if she bought ten times as many chickens as the number that died due to disease?"""
    initial_chickens = 400
    death_percent = 40
    death_count = initial_chickens * (death_percent / 100)
    bought_count = death_count * 10
    total_chickens = initial_chickens - death_count + bought_count
    result = total_chickens
    return result

print(solution())