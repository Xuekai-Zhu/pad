def solution():
    white_russian_ingredients = ['cream', 'vodka', 'Kahlua']
    curdling_ingredients = ['lime']
    compatible_ingredients = [ingredient for ingredient in white_russian_ingredients if ingredient not in curdling_ingredients]
    if 'kaffir lime' in compatible_ingredients:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())