def solution():
    # Let x be the length of the short side of the fence
    x = 1

    # Calculate the length of the other short side and the two long sides
    y = 3 * x
    z = 2 * y

    # Calculate the total length of the fence
    total_length = x + y + z

    # Calculate the length of the fence that needs to be replaced
    rusted_length = x
    new_length = 0
    for i in range(1, rusted_length+1):
        if i == rusted_length:
            new_length += y
        else:
            new_length += (3 * i) * 2

    # Calculate the total length of the new fence
    total_new_length = total_length - rusted_length + new_length

    # Calculate the length of the fence that needs to be replaced
    replaced_length = total_new_length - total_length

    result = replaced_length
    return result

print(solution())