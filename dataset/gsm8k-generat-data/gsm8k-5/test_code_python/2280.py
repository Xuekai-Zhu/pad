def solution():
    total_rope = 20  # Orlan has a 20-meter rope
    given_to_allan = total_rope / 4  # Orlan gave 1/4 of his rope to Allan
    remaining_rope = total_rope - given_to_allan  # Orlan has the remaining rope
    given_to_jack = (2 / 3) * remaining_rope  # Orlan gave 2/3 of the remaining rope to Jack
    remaining_rope -= given_to_jack  # Orlan has the remaining rope

    result = remaining_rope
    return result

print(solution())