def solution():
    # Define E.T.'s favorite candy and Friendly's desserts
    et_favorite_candy = "Reese's Pieces"
    friendlys_desserts = ["Reese's Peanut Butter Cup Sundae", "Reese's Pieces Sundae"]
    # Check if any of Friendly's desserts have E.T.'s favorite candy
    if et_favorite_candy in friendlys_desserts:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())