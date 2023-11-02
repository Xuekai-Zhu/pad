def solution():
    """Alexander draws 9 pictures for an exhibition at a gallery. 5 new galleries also want Alexander to draw for them, so he draws pictures for their exhibitions too. Each of these new galleries receives the same amount of pictures. 
    For each picture, Alexander needs 4 pencils. For each exhibition, he needs another 2 pencils for signing his signature on the pictures. If Alexander uses 88 pencils on drawing and signing his pictures for all of the exhibitions, how many paintings are at each of the 5 new galleries?"""
    total_pictures = 9 + (5 * x)  # Let x be the number of pictures at each new gallery
    total_pencils = 88
    pencils_per_picture = 4
    pencils_for_signature = 2
    
    # Find the total number of pencils needed for all the pictures
    pencils_for_pictures = total_pictures * pencils_per_picture
    
    # Find the total number of pencils needed for all the signatures
    pencils_for_signatures = (5 * pencils_for_signature)
    
    # Find the total number of pencils needed
    total_pencils_needed = pencils_for_pictures + pencils_for_signatures
    
    # Solve for x (number of pictures at each new gallery)
    x = (total_pictures - 9) / 5
    
    result = x
    return result

print(solution())