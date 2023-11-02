def solution():
    num_bags_50_beads = 5
    num_bags_100_beads = 2

    num_beads_50_beads_bag = 50
    num_beads_100_beads_bag = 100

    num_beads_total = (num_bags_50_beads * num_beads_50_beads_bag) + (num_bags_100_beads * num_beads_100_beads_bag)

    num_bracelets = num_beads_total // 50

    result = num_bracelets
    return result

print(solution())