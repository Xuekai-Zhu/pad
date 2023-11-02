def solution():
    """Mary is writing a story, and wants her 60 characters to be split according to their initials. Half of her characters have the initial A, and half of this amount have the initial C. Mary wants the rest of her characters to have the initials D and E, but she wants there to be twice as many characters with the initial D as there are characters with the initial E. How many of Mary's characters have the initial D?"""
    total_characters = 60
    half_a = total_characters // 2
    half_c = half_a // 2
    half_d_e = total_characters - half_a - half_c
    d = 2 * (half_d_e // 3)
    result = d
    return result

print(solution())