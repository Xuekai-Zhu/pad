def solution():
    # Calculate the number of popsicle sticks each person has
    steve_sticks = 12
    sid_sticks = steve_sticks * 2
    sam_sticks = sid_sticks * 3

    # Calculate the total number of popsicle sticks
    total_sticks = steve_sticks + sid_sticks + sam_sticks
    result = total_sticks
    return result

print(solution())