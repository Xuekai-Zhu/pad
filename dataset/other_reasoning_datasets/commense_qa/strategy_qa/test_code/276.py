def solution():
    original_categories = ["Chemistry", "Literature", "Peace", "Physics", "Physiology or Medicine"]
    new_categories = ["Economic Sciences"]
    all_categories = original_categories + new_categories
    if len(all_categories) == 6:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())