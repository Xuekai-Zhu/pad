def solution():
    """There are 920 deer in a park. 10% of the deer have 8 antlers, and a quarter of that number also have albino fur. How many albino 8-antlered deer are there?"""
    total_deer = 920
    eight_antlers_percent = 10
    eight_antlers_deer = total_deer * (eight_antlers_percent / 100)
    albino_percent = 25
    albino_eight_antlers = eight_antlers_deer * (albino_percent / 100)
    result = albino_eight_antlers
    return result

print(solution())