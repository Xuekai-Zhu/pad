def solution():
    beads_per_bag = [50, 100] # Marnie bought 5 bags of 50 beads and 2 bags of 100 beads
    number_of_bags = [5, 2]
    total_beads = sum([beads_per_bag[i] * number_of_bags[i] for i in range(len(beads_per_bag))])

    # Calculate the number of bracelets Marnie can make
    bracelets = total_beads // 50
    
    result = bracelets
    return result

print(solution())