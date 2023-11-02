def solution():
    hedgehog_diet = ["birds", "toads", "slugs", "snails"]
    animals_with_spinal_cords = ["birds", "toads"]
    for animal in hedgehog_diet:
        if animal not in animals_with_spinal_cords:
            result = "no"
            break
    else:
        result = "yes"
    return result

print(solution())