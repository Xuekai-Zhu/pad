def solution():
    """James decides to cut down some trees. In the first 2 days, he cuts down 20 trees each day. For the next 3 days his 2 brothers help him cut down trees. They cut 20% fewer trees per day than James. How many total trees were cut down?"""
    # Define the number of trees cut down by James in the first 2 days
    james_daily_trees = 20
    james_total_trees = james_daily_trees * 2

    # Calculate the number of trees cut down by James and his brothers for the next 3 days
    james_brothers_daily_trees = james_daily_trees * 0.8
    james_brothers_total_trees = (james_brothers_daily_trees * 2) + james_daily_trees

    # Calculate the total number of trees cut down
    total_trees = james_total_trees + james_brothers_total_trees

    # Return the result
    result = total_trees
    return result

print(solution())