def solution():
    mongoose_period = "Neogene"
    rhino_period = "Paleogene"
    if mongoose_period > rhino_period:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())