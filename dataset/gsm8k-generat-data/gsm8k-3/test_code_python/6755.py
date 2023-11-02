def solution():
    """Alexander draws 9 pictures for an exhibition at a gallery. 5 new galleries also want Alexander to draw for them, so he draws pictures for their exhibitions too.
    Each of these new galleries receives the same amount of pictures.
    For each picture, Alexander needs 4 pencils. For each exhibition, he needs another 2 pencils for signing his signature on the pictures.
    If Alexander uses 88 pencils on drawing and signing his pictures for all of the exhibitions, how many paintings are at each of the 5 new galleries?"""
    
    # Define the number of pictures for the first gallery
    first_gallery = 9
    
    # Define the number of pictures for each of the new galleries
    new_galleries = 5
    pencils_per_picture = 4
    pencils_for_signature = 2
    total_pencils = 88
    
    # Calculate the total number of pictures drawn
    total_pictures = first_gallery + new_galleries*x
    # where x is the number of pictures at each new gallery
    
    # Calculate the total number of pencils used
    total_pencils_used = total_pictures*pencils_per_picture + new_galleries*pencils_for_signature
    
    # Calculate the number of pictures at each new gallery
    x = (total_pencils - first_gallery*pencils_per_picture - new_galleries*pencils_for_signature)/new_galleries/pencils_per_picture
    
    result = x
    return result

print(solution())