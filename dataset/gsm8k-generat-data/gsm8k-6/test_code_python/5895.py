def solution():
    # Calculate the height Lisa and Jacob can jump
    lisa_jump = 2 * 6  # Lisa can jump double the height of Mark
    jacob_jump = 2 * lisa_jump  # Jacob can jump double the height of Lisa

    # Calculate the height James can jump
    james_jump = (2/3) * jacob_jump  # James jumps 2/3 as high as Jacob
    result = james_jump
    return result

print(solution())