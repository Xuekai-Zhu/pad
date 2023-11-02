def solution():
    frank_apples = 36
    susan_apples = frank_apples * 3

    # Calculate how many apples Susan gave out
    susan_gave_out = susan_apples / 2

    # Calculate how many apples Frank sold
    frank_sold = frank_apples / 3

    # Calculate how many apples they have left
    total_apples_left = frank_apples - frank_sold + susan_apples - susan_gave_out
    result = total_apples_left
    return result

print(solution())