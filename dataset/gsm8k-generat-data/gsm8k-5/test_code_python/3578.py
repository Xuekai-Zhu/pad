def solution():
    total_dresses = 48 # The number of their dresses combined is 48
    difference = 18 # Lisa has 18 more dresses than Ana
    ana_dresses = (total_dresses - difference) / 2 # Let the number of Ana's dresses be x. Then Lisa has x + 18 dresses. Their total dresses is x + x + 18 = 2x + 18 = total_dresses. Solving for x gives x = (total_dresses - difference) / 2

    result = ana_dresses
    return result

print(solution())