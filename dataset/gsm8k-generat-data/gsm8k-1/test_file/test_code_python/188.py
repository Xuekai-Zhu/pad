def solution():
    """Tom plants 10 trees a year. Every year he also chops down 2 trees a year. He starts with 50 trees. After 10 years 30% of the trees die. How many trees does he have left?"""
    starting_trees = 50
    yearly_growth = 10
    yearly_loss = 2
    years = 10
    remaining_trees = starting_trees + (yearly_growth - yearly_loss) * years
    dead_trees = int(0.3 * remaining_trees)
    trees_left = remaining_trees - dead_trees
    
    result = trees_left
    return result

print(solution())