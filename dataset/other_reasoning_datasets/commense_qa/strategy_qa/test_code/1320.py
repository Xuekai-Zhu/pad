def solution():
    reformation_tool = "nails"
    crucifixion_tools = ["nails", "wooden beam"]
    if reformation_tool in crucifixion_tools:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())