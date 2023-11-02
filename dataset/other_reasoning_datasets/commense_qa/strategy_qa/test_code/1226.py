def solution():
    greenhouse_plants = True
    warthog_food_sources = ["grasses", "roots", "berries", "small insects"]
    greenhouse_insects = ["aphids", "fungus gnats", "caterpillars"]
    if (not greenhouse_plants) or (any(insect in warthog_food_sources for insect in greenhouse_insects)):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())