def solution():
    wolverine_native_habitat = "northern boreal forests"
    miami_habitat = "not a northern boreal habitat"
    if wolverine_native_habitat not in miami_habitat:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())