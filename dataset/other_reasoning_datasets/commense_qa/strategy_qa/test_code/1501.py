def solution():
    geology_topics = ["gemstones", "minerals", "stone"]
    lapidary_materials = ["stone", "minerals", "gemstones"]
    overlap = [material for material in geology_topics if material in lapidary_materials]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())