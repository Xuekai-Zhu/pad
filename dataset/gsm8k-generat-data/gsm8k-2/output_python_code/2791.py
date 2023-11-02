def solution():
    """Liam is teaching art to a group of 10 students. He has 20 art kits that he hands out to the students to share, 1 art kit for 2 students. From those art kits half the students make 3 artworks each and half the students make 4 artworks each. How many artistic works does the whole class create?"""
    total_students = 10
    total_art_kits = 20
    artworks_per_kit = 2.5  # Half make 3, half make 4
    total_artworks = total_art_kits * artworks_per_kit
    result = total_artworks
    return result

print(solution())