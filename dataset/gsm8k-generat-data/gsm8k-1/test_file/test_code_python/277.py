def solution():
    """A cobra, which has 70 spots, has twice as many spots as a mamba. If there are 40 cobras and 60 mambas in a snake park, what is half the number of spots they all have combined?"""
    cobra_spots = 70
    mamba_spots = cobra_spots / 2
    num_cobras = 40
    num_mambas = 60
    total_spots = (cobra_spots * num_cobras) + (mamba_spots * num_mambas)
    half_total_spots = total_spots / 2
    result = half_total_spots
    return result

print(solution())