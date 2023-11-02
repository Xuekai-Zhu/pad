def solution():
    wine_cost = 20.00
    percent_increase = 25
    bottles = 5
    price_increase = wine_cost * (percent_increase / 100)
    new_ cost = wine_cost + price_increase
    total_cost = new_cost * bottles
    result = total_cost
    return result

print(solution())