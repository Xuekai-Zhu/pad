def solution():
    plants_produce_oxygen = True
    quartz_composition = ["silicon", "oxygen"]
    quartz_melting_point = "high"
    if not plants_produce_oxygen and "oxygen" in quartz_composition and quartz_melting_point == "high":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())