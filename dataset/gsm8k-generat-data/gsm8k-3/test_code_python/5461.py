def solution():
    """June's mom promises to pay her 1 cent for every cloverleaf she picks from the lawn. June picks 200 clovers in total. 75% have 3 petals. 24% have two petals and 1% have four petals. How many cents does June earn?"""
    # Define the value per clover leaf
    VALUE_PER_LEAF = 0.01

    # Calculate the number of clover leaves with 3 petals
    leaves_3petals = 0.75 * 200
    # Calculate the number of clover leaves with 2 petals
    leaves_2petals = 0.24 * 200
    # Calculate the number of clover leaves with 4 petals
    leaves_4petals = 0.01 * 200

    # Calculate the total number of clover leaves
    total_leaves = leaves_3petals + leaves_2petals + leaves_4petals

    # Calculate the total earnings
    earnings = total_leaves * VALUE_PER_LEAF

    # Display the total earnings
    result = earnings
    return result

print(solution())