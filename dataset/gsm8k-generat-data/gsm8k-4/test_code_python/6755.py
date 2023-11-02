def solution():
    """Alexander draws 9 pictures for an exhibition at a gallery. 5 new galleries also want Alexander to draw for them, so he draws pictures for their exhibitions too. Each of these new galleries receives the same amount of pictures. For each picture, Alexander needs 4 pencils. For each exhibition, he needs another 2 pencils for signing his signature on the pictures. If Alexander uses 88 pencils on drawing and signing his pictures for all of the exhibitions, how many paintings are at each of the 5 new galleries?"""

    # Define the number of pictures drawn for the first exhibition
    first_exhibition_pictures = 9

    # Define the total number of new galleries
    num_new_galleries = 5

    # Define the total number of pictures drawn for all the exhibitions
    total_pictures = first_exhibition_pictures + (num_new_galleries * x)

    # Define the total number of pencils needed for each picture and signature
    pencils_per_picture = 4
    pencils_per_signature = 2

    # Calculate the total number of pencils used
    total_pencils = pencils_per_picture * total_pictures + pencils_per_signature * (first_exhibition_pictures + num_new_galleries)

    # Calculate the number of pictures at each new gallery
    x = (total_pencils - pencils_per_signature * (first_exhibition_pictures + num_new_galleries)) / (pencils_per_picture * num_new_galleries)

    result = x
    return result

print(solution())