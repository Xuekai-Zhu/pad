def solution():
    macaque_height_range = range(16, 29)
    macaque_weight_range = range(12, 40)
    elephant_height_range = range(84, 132)
    elephant_weight_range = range(4000, 14000)
    if max(macaque_height_range) < min(elephant_height_range) and max(macaque_weight_range) < min(elephant_weight_range):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())