def solution():
    # Calculate the total number of beads Marnie bought
    total_beads = 5 * 50 + 2 * 100  # 5 bags of 50 beads and 2 bags of 100 beads
    # Calculate the total number of bracelets Marnie can make
    total_bracelets = total_beads // 50  # 50 beads are used to make one bracelet
    result = total_bracelets
    return result

print(solution())