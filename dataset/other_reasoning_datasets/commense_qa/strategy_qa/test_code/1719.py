def solution():
    ethiopian_cuisine = ["vegetables", "spicy meat dishes"]
    seafood = ["shrimp"]
    overlap = [dish for dish in ethiopian_cuisine if dish in seafood]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())