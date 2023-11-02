def solution():
    network_language = "Portuguese"
    anchor_languages = ["Portuguese", "English", "Spanish"]
    if "Chinese" in anchor_languages:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())