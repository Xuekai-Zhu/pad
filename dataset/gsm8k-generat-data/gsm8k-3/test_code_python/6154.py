def solution():
    """Mary is writing a story, and wants her 60 characters to be split according to their initials. Half of her characters have the initial A, and half of this amount have the initial C. Mary wants the rest of her characters to have the initials D and E, but she wants there to be twice as many characters with the initial D as there are characters with the initial E. How many of Mary’s characters have the initial D?"""
    # Calculate the number of characters with the initial A
    a_count = 60 // 2

    # Calculate the number of characters with the initial C
    c_count = a_count // 2

    # Calculate the number of characters with the initial D
    d_count = (60 - a_count - c_count) // 3 * 2

    # Display the number of characters with the initial D
    result = d_count
    return result

print(solution())