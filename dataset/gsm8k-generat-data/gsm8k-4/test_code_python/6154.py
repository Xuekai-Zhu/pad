def solution():
    """Mary is writing a story, and wants her 60 characters to be split according to their initials. Half of her characters have the initial A, and half of this amount have the initial C. Mary wants the rest of her characters to have the initials D and E, but she wants there to be twice as many characters with the initial D as there are characters with the initial E. How many of Mary’s characters have the initial D?"""
    # Define the total number of characters
    total_characters = 60

    # Calculate the number of characters with the initial A
    a_characters = total_characters // 2

    # Calculate the number of characters with the initial C
    c_characters = a_characters // 2

    # Calculate the number of characters with the initial D and E combined
    de_characters = total_characters - a_characters - c_characters

    # Calculate the number of characters with the initial E
    e_characters = de_characters // 3

    # Calculate the number of characters with the initial D
    d_characters = e_characters * 2

    result = d_characters
    return result

print(solution())