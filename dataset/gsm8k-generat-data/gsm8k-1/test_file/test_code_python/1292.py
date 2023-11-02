def solution():
    """Ellen and her sister, Lani, went to the mall to buy presents for their mom. Ellen bought a pair of leggings for $100 and a photo frame for $5. Lani bought a pair of sunglasses at $30 and two bathrobes at $100 each. How much did they spend in all?"""
    ellen_leggings = 100
    ellen_photo_frame = 5
    lani_sunglasses = 30
    lani_bathrobes = 2 * 100
    total_spent = ellen_leggings + ellen_photo_frame + lani_sunglasses + lani_bathrobes
    result = total_spent
    return result

print(solution())