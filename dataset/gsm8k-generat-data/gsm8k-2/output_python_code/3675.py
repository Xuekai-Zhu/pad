def solution():
    """Tabitha adds 1 serving of honey per cup of tea in the evening. She usually has 2 cups of tea before bed. She buys her honey in a 16-ounce container. If there are 6 servings of honey per ounce, how many nights will she be able to enjoy honey in her tea before bed?"""
    servings_per_cup = 1
    cups_per_night = 2
    ounces_in_container = 16
    servings_per_ounce = 6
    total_servings = servings_per_cup * cups_per_night * 7
    total_ounces = total_servings / servings_per_ounce
    nights = total_ounces / ounces_in_container
    result = nights
    return result

print(solution())