def solution():
    """There are 920 deer in a park. 10% of the deer have 8 antlers, and a quarter of that number also have albino fur. How many albino 8-antlered deer are there?"""
    total_deer = 920
    antlered_deer = 0.1 * total_deer
    albino_antlered_deer = 0.25 * antlered_deer
    result = albino_antlered_deer
    return result

print(solution())