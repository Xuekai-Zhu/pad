def solution():
    capacity = 16  # capacity of the USB drive is 16 GB
    used_space = 0.5 * capacity  # 50% is already busy
    available_space = capacity - used_space  # calculate the available space
    result = available_space
    return result

print(solution())