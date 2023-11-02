def solution():
    # Determine which churches recognize Alexander Nevsky as a saint
    russian_orthodox = True
    catholic = False
    ukrainian_greek_catholic = False
    
    # Check if the Ukrainian Greek Catholic Church recognizes Alexander Nevsky as a saint
    if russian_orthodox and not catholic and not ukrainian_greek_catholic:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())