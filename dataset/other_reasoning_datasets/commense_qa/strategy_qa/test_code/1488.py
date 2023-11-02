def solution():
    colitis_triggers = ["dairy", "alcohol", "caffeine"]
    if "caffeine" in colitis_triggers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())