def solution():
    unsafe_glaze_types = ["unsafe"]
    is_antique_pottery = True
    if "unsafe" in unsafe_glaze_types or is_antique_pottery:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())