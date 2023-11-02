def solution():
    initial_rope = 20
    given_to_allan = initial_rope / 4
    given_to_jack = (initial_rope - given_to_allan) / 3
    rope_left = initial_rope - given_to_allan - given_to_jack
    result = rope_left
    return result

print(solution())