def solution():
    """James and Lisa ordered 2 small pizzas. Each pizza has 6 slices. James ate 2/3 of all the slices. How many slices of pizza did James eat?"""
    num_pizzas = 2
    slices_per_pizza = 6
    total_slices = num_pizzas * slices_per_pizza
    james_slices = total_slices * (2/3)
    result = james_slices
    return result

print(solution())