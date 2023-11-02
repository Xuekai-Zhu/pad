def solution():
    """For the children's day celebration, children are to perform mass drills in the presence of the President of the country. They stand 8 in a row and there are 7 rows each for 5 different Schools. How many children can there be in the drill?"""
    children_per_row = 8
    rows_per_school = 7
    num_schools = 5
    total_children = children_per_row * rows_per_school * num_schools
    result = total_children
    return result

print(solution())