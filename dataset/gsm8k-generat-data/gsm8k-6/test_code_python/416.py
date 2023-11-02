def solution():
    # Calculate the depth of the river by mid-July
    depth_june = 5 + 10  # the river is 10 feet deeper than mid-May by mid-June
    depth_july = 3 * depth_june  # the river is three times deeper than mid-June by mid-July
    result = depth_july
    return result

print(solution())