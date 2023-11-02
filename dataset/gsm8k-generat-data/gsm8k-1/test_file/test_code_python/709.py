def solution():
    """Mr Boarden is remodeling his bathroom. For every square foot, he needs 24 mosaic tiles. How many mosaic tiles would Mr Boarden need to cover two thirds of his 36 sq ft bathroom?"""
    sq_ft_bathroom = 36
    sq_ft_to_cover = sq_ft_bathroom * (2/3)
    tiles_per_sq_ft = 24
    total_tiles_needed = sq_ft_to_cover * tiles_per_sq_ft
    result = total_tiles_needed
    return result

print(solution())