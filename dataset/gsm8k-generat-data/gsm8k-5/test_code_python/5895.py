def solution():
    mark_jump = 6  # Mark can jump 6 inches off the ground
    lisa_jump = mark_jump * 2  # Lisa can jump double the height of Mark
    jacob_jump = lisa_jump * 2  # Jacob can jump double the height of Lisa
    james_jump = jacob_jump * 2 / 3  # James can jump 2/3 as high as Jacob

    result = james_jump
    return result

print(solution())