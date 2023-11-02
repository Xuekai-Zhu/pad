def solution():
    """A crayon factory makes 4 colors of crayons. They put 2 of each color crayon in each box. The factory produces enough crayons to fill 5 boxes per hour. How many crayons does the factory produce in 4 hours?"""
    # Define the number of colors of crayons
    num_colors = 4

    # Define the number of crayons of each color in each box
    num_crayons_per_color = 2

    # Define the number of boxes produced per hour
    boxes_per_hour = 5

    # Calculate the number of crayons produced per hour
    crayons_per_hour = num_colors * num_crayons_per_color * boxes_per_hour

    # Calculate the number of crayons produced in 4 hours
    crayons_per_4_hours = crayons_per_hour * 4

    result = crayons_per_4_hours
    return result

print(solution())