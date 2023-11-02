def solution():
    """Frank picked 36 apples. Susan picked 3 times as many apples as Frank. If Susan gave out half of her apples, and Frank sold a third of his, how many in total do they have left?"""
    # Define the number of apples picked by Frank
    frank_apples = 36

    # Define the number of apples picked by Susan
    susan_apples = frank_apples * 3

    # Calculate the number of apples Susan gave out
    susan_gave_out = susan_apples / 2

    # Calculate the number of apples Frank sold
    frank_sold = frank_apples / 3

    # Calculate the total number of apples left
    total_apples = frank_apples + susan_apples - susan_gave_out - frank_sold

    # Display the total number of apples left
    result = total_apples
    return result

print(solution())