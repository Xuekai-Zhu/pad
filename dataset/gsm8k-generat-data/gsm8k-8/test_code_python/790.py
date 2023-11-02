def solution():
    # Define the base and height of Zion's triangle
    zion_base = 40
    zion_height = 20

    # Calculate the area of Zion's triangle
    zion_area = 0.5 * zion_base * zion_height

    # Calculate the base and height of Zion's friends' triangles
    friend_base = zion_base
    friend_height = zion_height

    # Calculate the area of Zion's friends' triangles
    friend_area = 0.5 * friend_base * friend_height

    # Calculate the total area of the three triangles
    total_area = zion_area + 2 * friend_area
    result = total_area
    return result

print(solution())