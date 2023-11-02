def solution():
    """Steve has 2 boxes of pencils with 12 pencils in each box. He gave Matt 3 more pencils than he gave to Lauren. If Steve gave 6 pencils to Lauren, how many pencils does he have left?"""
    boxes = 2
    pencils_per_box = 12
    total_pencils = boxes * pencils_per_box
    pencils_to_lauren = 6
    pencils_to_matt = pencils_to_lauren + 3
    pencils_given_away = pencils_to_lauren + pencils_to_matt
    pencils_left = total_pencils - pencils_given_away
    result = pencils_left
    return result

print(solution())