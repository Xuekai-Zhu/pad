def solution():
    watermelon_climates = ["tropical", "temperate"]
    antarctica_climate = "coldest"
    brazil_climate = "tropical"
    if brazil_climate in watermelon_climates and antarctica_climate not in watermelon_climates:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())