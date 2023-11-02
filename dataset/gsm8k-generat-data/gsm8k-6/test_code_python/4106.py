def solution():
    # Find the total number of cans collected by Juwan, since Solomon collected 3 times as many cans as Juwan
    cans_Juwan = 66 / 3  

    # Find the total number of cans collected by Levi, since Levi collected half of what Juwan collected
    cans_Levi = cans_Juwan / 2  

    # Find the total number of cans collected by all the boys
    total_cans = 66 + cans_Juwan + cans_Levi

    result = total_cans
    return result

print(solution())