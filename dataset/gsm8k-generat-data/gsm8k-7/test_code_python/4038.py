def solution():
    final_geese = 12

    # Calculate the number of geese that landed in the trees
    landed_geese = (1/2) * final_geese

    # Calculate the number of geese in the new V formation
    new_v_geese = final_geese - landed_geese

    # Calculate the number of geese in the original formation
    original_geese = new_v_geese - 4
    result = original_geese
    return result

print(solution())