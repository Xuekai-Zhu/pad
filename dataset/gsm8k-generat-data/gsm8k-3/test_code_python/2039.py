def solution():
    """Leo had 400 marbles in a jar. He packed the marbles with ten marbles in each pack, and he gave some of them to his two friends,  Manny and Neil.   He gave Manny 1/4 of the number of packs of marbles, Neil received 1/8 of the number of packs of marbles, and he kept the rest. How many packs of marbles did Leo keep?"""
    # Define the number of marbles in the jar and the number of marbles per pack
    marbles = 400
    marbles_per_pack = 10
    
    # Calculate the total number of packs
    total_packs = marbles // marbles_per_pack
    
    # Calculate the number of packs given to Manny and Neil
    manny_packs = total_packs // 4
    neil_packs = total_packs // 8
    
    # Calculate the number of packs Leo kept
    leo_packs = total_packs - manny_packs - neil_packs
    
    # Display the number of packs Leo kept
    result = leo_packs
    return result

print(solution())