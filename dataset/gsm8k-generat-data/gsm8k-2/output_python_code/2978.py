def solution():
    """Barbeck has two times as many guitars as Steve, but Davey has three times as many guitars as Barbeck. If there are 27 guitars altogether, how many guitars does Davey have?"""
    total_guitars = 27
    barbeck_guitars = total_guitars / (2 + 1 + 3)
    davey_guitars = 3 * barbeck_guitars
    result = davey_guitars
    return result

print(solution())