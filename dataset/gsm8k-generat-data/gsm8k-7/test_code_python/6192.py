def solution():
    total_apples = 18

    # Split the apples evenly between Greg and Sarah
    greg_apples = total_apples // 2
    sarah_apples = total_apples // 2

    # Susan has twice as many apples as Greg
    susan_apples = greg_apples * 2

    # Mark has 5 fewer apples than Susan
    mark_apples = susan_apples - 5

    # Calculate the total number of apples available for the apple pie
    total_available_apples = greg_apples + sarah_apples + susan_apples + mark_apples

    # Calculate the number of apples left over after making the apple pie
    apples_left_over = total_available_apples - 40

    result = apples_left_over
    return result

print(solution())