def solution():
    bronze_age_start = 3300
    bronze_age_end = 300
    gunpowder_discovered = 9
    if bronze_age_end < gunpowder_discovered:
        result = "no"
    else:
        materials_known = ["iron"]
        result = "yes" if all(material in materials_known for material in ["fuse", "gunpowder", "iron"]) else "no"
    return result

print(solution())