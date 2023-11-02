def solution():
    """One US cup equals 250ml. Brian is making lasagna for himself, his wife, his two kids, his parents, and his wife's parents. The recipe requires 1/2 a cup of milk per serving. How many 1L cartons of milk does Brian need to buy if each person is expected to eat 2 servings?"""
    total_people = 6
    servings_per_person = 2
    total_servings = total_people * servings_per_person
    milk_per_serving = 0.5 # in cups
    milk_per_person = milk_per_serving * 250 # in ml
    total_milk_required = milk_per_person * total_people
    milk_carton_size = 1000 # in ml
    milk_cartons_required = total_milk_required / milk_carton_size
    milk_cartons_required = round(milk_cartons_required + 0.5) # rounding up to nearest integer
    result = milk_cartons_required
    return result

print(solution())