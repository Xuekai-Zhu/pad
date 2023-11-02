def solution():
    """Shawnda decides that her neighborhood kids could really use a bike inflation service. She decides the best way to charge is by the tire. Each tire costs 25 cents to inflate. On the first day, 5 people on bicycles came by to get both tires inflated. 3 people came by to get all their tricycle tires inflated. Finally, one person actually came by on a unicycle. How many dollars did she make that day?"""
    biker_count = 5
    biker_tire_count = 2
    tricycle_count = 3
    tricycle_tire_count = 3
    unicycle_count = 1
    tire_count = (biker_tire_count * biker_count) + (tricycle_tire_count * tricycle_count) + unicycle_count
    price_per_tire = 0.25
    total_price = tire_count * price_per_tire
    result = total_price
    return result

print(solution())