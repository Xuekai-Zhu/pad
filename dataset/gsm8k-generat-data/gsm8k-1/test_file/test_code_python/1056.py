def solution():
    """Becky, Jake, and Silvia shared 4 pizzas. Each pizza had 8 slices. Becky ate 3 more slices than Jake did. Silvia ate twice as many slices than Jake did. If Becky ate 10 slices, how many total slices did they eat?"""
    pizzas = 4
    slices_per_pizza = 8
    becky_slices = 10
    jake_slices = becky_slices - 3
    silvia_slices = jake_slices * 2
    total_slices = (becky_slices + jake_slices + silvia_slices) * pizzas
    result = total_slices
    return result

print(solution())