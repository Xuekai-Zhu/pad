def solution():
    total_apples = 18  # Greg and Sarah have 18 apples to split evenly
    greg_apples = total_apples // 2  # Greg gets half of the apples
    susan_apples = greg_apples * 2  # Susan has twice as many apples as Greg
    mark_apples = susan_apples - 5  # Mark has 5 fewer apples than Susan

    # Calculate the total number of apples among all of them
    total_apples = greg_apples + susan_apples + mark_apples

    # Calculate the number of apples left over after making the pie
    apples_left_over = total_apples - 40
    result = apples_left_over
    return result

print(solution())