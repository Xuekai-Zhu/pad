def solution():
    # Calculate the total number of beads Nancy has
    total_Nancy_beads = 40 + 20  # 20 more pearl beads than metal beads

    # Calculate the total number of beads Rose has
    total_Rose_beads = 20 + 2*20  # twice as many stone beads as crystal beads

    # Calculate the total number of bracelets Nancy and Rose can make
    total_bracelets = (total_Nancy_beads + total_Rose_beads) // 8  # 8 beads in each bracelet
    result = total_bracelets
    return result

print(solution())