def solution():
    """John with his five friends ordered 3 pizzas. Each pizza had 8 slices. If they all finished and ate the same amount of pizzas, how many slices did each person eat?"""
    num_people = 6  # John and his 5 friends
    num_pizzas = 3
    slices_per_pizza = 8
    total_slices = num_pizzas * slices_per_pizza
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())