def solution():
    """Arnel had ten boxes of pencils with the same number of pencils in each box. He kept ten pencils and shared the remaining pencils equally with his five friends. If his friends got eight pencils each, how many pencils are in each box?"""
    total_pencils = 10 * (8+5) + 10
    pencils_per_box = total_pencils // 10
    return pencils_per_box

print(solution())