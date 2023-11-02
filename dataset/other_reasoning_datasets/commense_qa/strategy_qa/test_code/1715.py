def solution():
    pancake_cooking_tools = ["pot", "griddle", "skillet"]
    appropriate_tools = ["griddle", "skillet"]
    overlap = [tool for tool in pancake_cooking_tools if tool in appropriate_tools]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())