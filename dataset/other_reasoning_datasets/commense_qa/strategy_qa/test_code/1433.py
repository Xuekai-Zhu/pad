def solution():
    character_name = "Bugs Bunny"
    carried_item = "carrot"
    item_category = "root vegetable"
    if carried_item == item_category:
        result = f"{character_name} is known for carrying a {item_category} around with him."
    else:
        result = f"{character_name} is not known for carrying a {item_category} around with him."
    return result

print(solution())