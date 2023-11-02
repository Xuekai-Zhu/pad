def solution():
    """Ben has 4 tubes of blue paint and 3 tubes of yellow paint. Jasper has half as many tubes of blue paint as Ben, and three times as many tubes of yellow paint as Ben. How many tubes of paint does Jasper have?"""
    ben_blue_paint = 4
    ben_yellow_paint = 3
    jasper_blue_paint = ben_blue_paint / 2
    jasper_yellow_paint = ben_yellow_paint * 3
    total_paint = jasper_blue_paint + jasper_yellow_paint
    result = total_paint
    return result

print(solution())