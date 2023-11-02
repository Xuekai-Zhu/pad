def solution():
    """James decides to cut down some trees.  In the first 2 days, he cuts down 20 trees each day.  For the next 3 days his 2 brothers help him cut down trees.  They cut 20% fewer trees per day than James.  How many total trees were cut down?"""
    # Calculate the total number of trees cut down by James in the first 2 days
    james_trees_first_two_days = 20 * 2

    # Calculate the percentage of trees cut down per day by James' brothers
    james_cut_rate = 20
    brother_cut_rate = james_cut_rate * 0.8

    # Calculate the total number of trees cut down by James and his brothers in the next 3 days
    brothers_trees_next_three_days = brother_cut_rate * 3
    total_trees_next_three_days = james_cut_rate + brothers_trees_next_three_days

    # Calculate the total number of trees cut down
    total_trees_cut_down = james_trees_first_two_days + total_trees_next_three_days

    # Display the total number of trees cut down
    result = total_trees_cut_down
    return result

print(solution())