def solution():
    # Calculate the number of legos Simon has
    kent_legos = 40
    bruce_legos = kent_legos + 20
    simon_legos = int(bruce_legos * 1.2)  # Simon has 20% more legos than Bruce
    result = simon_legos
    return result

print(solution())