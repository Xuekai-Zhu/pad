def solution():
    """Johnny buys 15 packs of colored pencils for his class. Each pack has a red, yellow, and green pencil inside. When he gets home he notices that 3 of the packs have two extra red pencils inside. How many red colored pencils did Johnny buy?"""
    # Define the total number of packs and pencils
    total_packs = 15
    pencils_per_pack = 3

    # Calculate the total number of red pencils
    total_red_pencils = total_packs * pencils_per_pack

    # Calculate the number of packs with extra red pencils
    packs_with_extra_red = 3

    # Calculate the total number of extra red pencils
    extra_red_pencils = 2 * packs_with_extra_red

    # Calculate the final total number of red pencils
    final_red_pencils = total_red_pencils + extra_red_pencils - (pencils_per_pack * packs_with_extra_red)

    # Return the result
    result = final_red_pencils
    return result

print(solution())