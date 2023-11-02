def solution():
    """Lisa is a member of the photography club at school. Every weekend the club will go anywhere to take photos. Leslie took 10 photos of animals to share with the club. She also took 3 times as many photos of flowers as animals and took 10 fewer scenery than the flowers. If Lisa took 15 fewer photos last weekend, How many photos did she take then?"""
    # Number of photos of animals
    animals = 10

    # Number of photos of flowers (3 times the number of animals)
    flowers = animals * 3

    # Number of photos of scenery (10 less than flowers)
    scenery = flowers - 10

    # Total number of photos taken by Leslie
    total_photos = animals + flowers + scenery

    # Lisa took 15 fewer photos than Leslie
    lisa_photos = total_photos - 15

    # Display the number of photos Lisa took
    result = lisa_photos
    return result

print(solution())