def solution():
    """Mr. Zubir bought a pair of pants, a shirt, and a coat. The pair of pants and shirt costs $100. The pants and coat cost $244. The coat costs 5 times as much as the shirt. How much did Mr. Zubir pay for his coat?"""
    pants_and_shirt_cost = 100
    pants_and_coat_cost = 244
    coat_cost = 0
    for i in range(1, 6):
        if i * pants_and_shirt_cost + pants_and_coat_cost == i * (2 * pants_and_shirt_cost + coat_cost):
            coat_cost = i * pants_and_shirt_cost + pants_and_coat_cost - 2 * pants_and_shirt_cost
            break
    result = coat_cost
    return result

print(solution())