def solution():
    """Alexander draws 9 pictures for an exhibition at a gallery. 5 new galleries also want Alexander to draw for them, so he draws pictures for their exhibitions too. Each of these new galleries receives the same amount of pictures. For each picture, Alexander needs 4 pencils. For each exhibition, he needs another 2 pencils for signing his signature on the pictures. If Alexander uses 88 pencils on drawing and signing his pictures for all of the exhibitions, how many paintings are at each of the 5 new galleries?"""
    total_pictures = 9 + 5 * x
    total_pencils = 4 * total_pictures + 2 * 5 * x
    # Solve for x
    x = (88 - 4 * 9) / (4 * 5 + 2 * 5)
    paintings_at_each_gallery = x
    result = paintings_at_each_gallery
    return result

print(solution())