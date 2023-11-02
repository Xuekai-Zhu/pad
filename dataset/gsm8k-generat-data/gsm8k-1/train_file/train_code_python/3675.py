def solution():
    """Tabitha adds 1 serving of honey per cup of tea in the evening. She usually has 2 cups of tea before bed. She buys her honey in a 16-ounce container. If there are 6 servings of honey per ounce, how many nights will she be able to enjoy honey in her tea before bed?"""
    servings_of_honey_per_cup = 1
    cups_of_tea_per_night = 2
    ounces_in_container = 16
    servings_of_honey_per_ounce = 6
    total_servings_of_honey = servings_of_honey_per_cup * cups_of_tea_per_night * 7
    total_ounces_of_honey_needed = total_servings_of_honey / servings_of_honey_per_ounce
    nights_of_honey = total_ounces_of_honey_needed / ounces_in_container
    result = int(nights_of_honey)
    return result

print(solution())