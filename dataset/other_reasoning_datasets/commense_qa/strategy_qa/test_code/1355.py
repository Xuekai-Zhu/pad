def solution():
    yubiwa_pipe = True
    finger_size = "small"
    ankle_size = "large"
    if yubiwa_pipe and finger_size < ankle_size:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())