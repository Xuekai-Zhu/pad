def solution():
    rope_length = 20
    quarter_length = rope_length / 4
    remaining_length = rope_length - quarter_length
    jack_length = 2/3 * remaining_length
    orlan_length = remaining_length - jack_length
    result = orlan_length
    return result

print(solution())