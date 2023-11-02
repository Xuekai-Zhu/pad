def solution():
    """Lisa is a member of the photography club at school. Every weekend the club will go anywhere to take photos. Leslie took 10 photos of animals to share with the club. She also took 3 times as many photos of flowers as animals and took 10 fewer scenery than the flowers. If Lisa took 15 fewer photos last weekend, How many photos did she take then?"""
    animals = 10
    flowers = animals * 3
    scenery = flowers - 10
    total_photos = animals + flowers + scenery
    
    # Lisa took 15 fewer photos than the total last weekend
    lisa_photos = total_photos - 15
    
    result = lisa_photos
    return result

print(solution())