def solution():
    strawberry_diseases = ["black root rot", "nematodes"]
    dog_worms = ["roundworms", "ascarids"]
    nematodes_are_roundworms = True
    if nematodes_are_roundworms and "nematodes" in strawberry_diseases:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())