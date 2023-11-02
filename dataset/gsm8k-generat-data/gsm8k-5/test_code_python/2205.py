def solution():
    frank_apples = 36  # Frank picked 36 apples
    susan_apples = 3 * frank_apples  # Susan picked 3 times as many apples as Frank

    susan_apples = susan_apples / 2  # Susan gave out half of her apples
    frank_apples = frank_apples / 3  # Frank sold a third of his apples

    # Calculate the total number of apples they have left
    total_apples_left = frank_apples + susan_apples
    result = total_apples_left
    return result

print(solution())