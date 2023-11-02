def solution():
    is_mario_64_licensed = True
    has_nintendo_copyright = True
    is_downloading_on_emulator = True
    if is_mario_64_licensed and has_nintendo_copyright and is_downloading_on_emulator:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())