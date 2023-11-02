def solution():
    limbs_required = ["arms", "legs"]
    # Check if all required limbs are present for jujutsu
    if "arms" in limbs_required and "legs" in limbs_required:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())