def solution():
    """Lisa is a member of the photography club at school. Every weekend the club will go anywhere to take photos. Leslie took 10 photos of animals to share with the club. She also took 3 times as many photos of flowers as animals and took 10 fewer scenery than the flowers. If Lisa took 15 fewer photos last weekend, How many photos did she take then?"""
    # Define the number of photos Leslie took of animals
    animals = 10

    # Calculate the number of photos Leslie took of flowers
    flowers = animals * 3

    # Calculate the number of photos Leslie took of scenery
    scenery = flowers - 10

    # Calculate the total number of photos Leslie took
    total_photos = animals + flowers + scenery

    # Calculate the number of photos Lisa took last weekend
    lisa_photos = total_photos - 15

    # Return the result
    result = lisa_photos
    return result

print(solution())