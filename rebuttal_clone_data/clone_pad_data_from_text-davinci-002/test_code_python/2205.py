def solution():
    frank_apples = 36
    susan_apples = frank_apples * 3
    susan_given_away = susan_apples / 2
    frank_sold = frank_apples / 3
    total_apples = susan_apples - susan_given_away + frank_apples - frank_sold
    result = total_apples
    
    return result

print(solution())