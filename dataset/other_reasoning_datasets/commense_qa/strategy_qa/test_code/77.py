def solution():
    ingredients = ["bacon", "lettuce", "tomato"]
    is_pork = any("pork" in ingredient for ingredient in ingredients)
    is_casablanca_muslim = True
    if is_pork and is_casablanca_muslim:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())