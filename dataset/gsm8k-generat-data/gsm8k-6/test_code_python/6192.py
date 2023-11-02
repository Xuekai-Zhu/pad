def solution():
    # Find the number of apples Greg and Sarah each receive
    greg_sarah_apples = 18 / 2  

    # Find the number of apples Susan has
    susan_apples = greg_sarah_apples * 2  

    # Find the number of apples Mark has
    mark_apples = susan_apples - 5  

    # Find the total number of apples after distribution
    total_apples = greg_sarah_apples * 2 + mark_apples  

    # Find the number of leftover apples after making the apple pie
    leftover_apples = total_apples - 40  
    result = leftover_apples
    return result

print(solution())