def solution():
    # Calculate the number of apples picked by Susan
    susan_picked = 3 * 36

    # Calculate the number of apples Susan has left after giving out half
    susan_left = susan_picked / 2

    # Calculate the number of apples Frank sold
    frank_sold = 36 / 3

    # Calculate the total number of apples they have left
    total_left = susan_left + (36 - frank_sold)

    result = total_left
    return result

print(solution())