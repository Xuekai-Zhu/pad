def solution():
    """A candy store uses food colouring in various candies. Each lollipop uses 5ml of food colouring, and each hard candy also needs food colouring. In one day, the candy store makes 100 lollipops and 5 hard candies. They do not use food colouring in anything else. The store has used 600ml of food colouring by the end of the day. How much food colouring, in millilitres, does each hard candy need?"""
    # Define the amount of food coloring per lollipop
    LOLLIPOP_COLORING = 5

    # Define the number of lollipops and hard candies made
    lollipop_count = 100
    hard_candy_count = 5

    # Define the total amount of food coloring used
    total_coloring_used = 600

    # Calculate the amount of food coloring used by the lollipops
    lollipop_coloring_used = lollipop_count * LOLLIPOP_COLORING

    # Calculate the amount of food coloring used by the hard candies
    hard_candy_coloring_used = total_coloring_used - lollipop_coloring_used

    # Calculate the amount of food coloring used per hard candy
    hard_candy_coloring_per_piece = hard_candy_coloring_used / hard_candy_count

    # Display the amount of food coloring used per hard candy
    result = hard_candy_coloring_per_piece
    return result

print(solution())