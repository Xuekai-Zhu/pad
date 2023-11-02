def solution():
    """Jim has 2 rows of 4 trees to start. When he turns 10 he decides to plant a new row of trees every year on his birthday. On his 15th birthday after he doubles the number of trees he has. How many trees does he have?"""
    starting_trees = 2 * 4
    yearly_growth = 1
    birthday_growth = 1
    current_age = 15
    end_age = current_age - 10
    total_trees = starting_trees
    for i in range(1, end_age):
        total_trees += 4 + yearly_growth
        yearly_growth += 1
    total_trees *= 2
    result = total_trees
    return result

print(solution())