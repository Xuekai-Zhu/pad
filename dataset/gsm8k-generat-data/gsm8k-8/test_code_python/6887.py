def solution():
    # Calculate the number of baby guppies in dozens
    baby_guppies_dozen = 3
    # Convert dozens to individual guppies
    baby_guppies = baby_guppies_dozen * 12
    # Add the 9 additional baby guppies
    baby_guppies += 9
    # Add the initial 7 guppies
    total_guppies = baby_guppies + 7
    result = total_guppies
    return result

print(solution())