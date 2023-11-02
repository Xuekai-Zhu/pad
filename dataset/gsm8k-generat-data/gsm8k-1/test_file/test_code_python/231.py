def solution():
    """John orders some pizzas to share with his friends. There are 20 friends in total, and John wants to make sure each can have 4 slices. Pizzas are only sold sliced into 8 portions. How many Pizzas does John need to order?"""
    friends = 20
    slices_per_person = 4
    slices_per_pizza = 8
    total_slices_needed = friends * slices_per_person
    pizzas_needed = total_slices_needed / slices_per_pizza
    result = pizzas_needed
    return result

print(solution())