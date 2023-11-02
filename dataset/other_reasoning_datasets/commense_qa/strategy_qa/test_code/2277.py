def solution():
    alice_published = 1865
    macbeth_first_performed = 1606
    if alice_published < macbeth_first_performed:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())