def solution():
    # Find the number of cats remaining after the first relocation
    cats_remaining = 1800 - 600

    # Find the number of cats relocated on the second mission
    cats_relocated = cats_remaining / 2

    # Find the number of cats remaining after the second mission
    cats_remaining -= cats_relocated

    result = cats_remaining
    return result

print(solution())