def solution():
    chef_name = "Masaharu Morimoto"
    cuisine_type = "Japanese"
    seaweed_ingredients = True
    glutamic_acid_flavoring = True
    if chef_name == "Masaharu Morimoto" and cuisine_type == "Japanese" and seaweed_ingredients and glutamic_acid_flavoring:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())