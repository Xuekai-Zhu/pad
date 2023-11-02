def solution():
    combined_length = 64
    bill_length = combined_length * 3 / 4   # since Jenna's eel is 1/3 as long as Bill's, Bill's eel would be 3/3 or 1 whole unit, so Jenna's eel would be 1/3 of that or 1/3 unit. Combined, they would be 4/4 or 1 whole unit so Bill's eel would be 3/4 of the total length
    jenna_length = combined_length - bill_length
    result = jenna_length
    return result

print(solution())