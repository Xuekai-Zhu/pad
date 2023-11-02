def solution():
    """Frank picked 36 apples. Susan picked 3 times as many apples as Frank. If Susan gave out half of her apples, and Frank sold a third of his, how many in total do they have left?"""
    # Define the initial number of apples picked by Frank and Susan
    frank_apples = 36
    susan_apples = frank_apples * 3

    # Susan gives out half of her apples
    susan_apples /= 2

    # Frank sells a third of his apples
    frank_apples *= 2/3

    # Calculate the total number of apples left
    total_apples = frank_apples + susan_apples

    result = total_apples
    return result

print(solution())