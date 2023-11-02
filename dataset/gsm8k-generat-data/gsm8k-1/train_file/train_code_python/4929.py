def solution():
    """James decides to cut down some trees. In the first 2 days, he cuts down 20 trees each day. For the next 3 days his 2 brothers help him cut down trees. They cut 20% fewer trees per day than James. How many total trees were cut down?"""
    james_trees_per_day = 20
    james_days = 2
    james_total_trees = james_trees_per_day * james_days
    brothers_trees_per_day = 0.8 * james_trees_per_day # 20% fewer trees
    brothers_days = 3
    brothers_total_trees = brothers_trees_per_day * brothers_days
    total_trees = james_total_trees + brothers_total_trees
    result = total_trees
    return result

print(solution())