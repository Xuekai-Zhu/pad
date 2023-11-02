def solution():
    # Define the number of apples picked by Frank and Susan
    frank_apples = 36
    susan_apples = 3 * frank_apples

    # Calculate the number of apples Susan gave away
    susan_gave_away = susan_apples / 2

    # Calculate the number of apples Frank sold
    frank_sold = frank_apples / 3

    # Calculate the total number of apples left
    total_apples_left = frank_apples + susan_apples - susan_gave_away - frank_sold
    result = total_apples_left
    return result

print(solution())