def solution():
    # Lanugo is found all over a baby's body but is usually shed before birth
    # Check if lanugo could potentially grow on the upper lip
    potential_lip_growth = True
    
    # Check if any known cases exist of a baby having lanugo on their upper lip
    known_cases = False
    
    if potential_lip_growth and known_cases:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())