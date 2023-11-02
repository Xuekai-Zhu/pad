def solution():
    # Define the textures of Kirby and English cucumbers
    kirby_texture = "bumpy"
    english_texture = "ridged"
    # Check if all cucumbers have the same texture
    if kirby_texture == english_texture:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())