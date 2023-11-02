def solution():
    # Define if a black widow woman would have any use for peaches
    has_use_for_peaches = False
    # Since peach pits contain cyanide and black widow women are known for poisoning their spouses, they may have use for peaches
    if "cyanide" in "peach pits" and "murders" in "black widow woman":
        has_use_for_peaches = True
    if has_use_for_peaches:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())