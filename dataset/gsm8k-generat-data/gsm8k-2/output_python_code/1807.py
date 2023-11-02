def solution():
    """The kids in Ms. Swanson's class have an average of 5 zits each. The kids in Mr. Jones' class have an average of six zits each. If there are 25 kids in Ms. Swanson's class and 32 in Mr. Jones' class, how many more zits are there in Mr. Jones' class than in Ms. Swanson's?"""
    ms_swanson_kids = 25
    mr_jones_kids = 32
    ms_swanson_zits = ms_swanson_kids * 5
    mr_jones_zits = mr_jones_kids * 6
    difference = mr_jones_zits - ms_swanson_zits
    result = difference
    return result

print(solution())