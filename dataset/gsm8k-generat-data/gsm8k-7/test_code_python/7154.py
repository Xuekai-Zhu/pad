def solution():
    alexis_pants = 21
    alexis_dresses = 18
    isabella_pants = alexis_pants / 3
    isabella_dresses = alexis_dresses / 3

    total_pants = alexis_pants + isabella_pants
    total_dresses = alexis_dresses + isabella_dresses

    result = total_pants + total_dresses
    return result

print(solution())