def solution():
    """Arnel had ten boxes of pencils with the same number of pencils in each box. He kept ten pencils and shared the remaining pencils equally with his five friends. If his friends got eight pencils each, how many pencils are in each box?"""
    friends = 5
    pencils_per_friend = 8
    total_pencils = friends * pencils_per_friend + 10
    boxes = 10
    pencils_per_box = (total_pencils - 10) / boxes
    result = pencils_per_box
    return result

print(solution())