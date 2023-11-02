def solution():
    garfield_favorite_food = "lasagna"
    italian_cuisine = "traditional Italian dish"
    if garfield_favorite_food == "lasagna" and italian_cuisine in garfield_favorite_food:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())