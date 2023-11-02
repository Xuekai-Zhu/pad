def solution():
    
    frank_apples = 36
    susan_apples = 3 * frank_apples
    susan_gave_away = susan_apples / 2
    frank_sold = frank_apples / 3

    total_left = frank_apples + susan_apples - susan_gave_away - frank_sold
    result = total_left
    return result

print(solution())