def solution():
    paleo_friendly_ingredients = ["ingredients found during the Paleolithic era"]
    cookie_ingredients = ["chocolate chips", "soy lecithin", "artificial grains"]
    for ingredient in cookie_ingredients:
        if ingredient in paleo_friendly_ingredients:
            result = "no"
            break
    else:
        result = "yes"
    return result

print(solution())