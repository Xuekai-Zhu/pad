def solution():
    branches = 30
    twigs_per_branch = 90
    twigs_sprouting_four_leaves = twigs_per_branch * .30
    twigs_sprouting_five_leaves = twigs_per_branch - twigs_sprouting_four_leaves
    leaves_on_four_twig_branches = twigs_sprouting_four_leaves * 4
    leaves_on_five_twig_branches = twigs_sprouting_five_leaves * 5
    total_leaves = leaves_on_five_twig_branches + leaves_on_four_twig_branches
    
    return total_leaves

print(solution())