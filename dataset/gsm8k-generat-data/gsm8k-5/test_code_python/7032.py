def solution():
    donuts_per_dozen = 12  # There are 12 donuts in a dozen
    donuts_per_half_dozen = 6  # There are 6 donuts in a half dozen
    total_donuts = 2.5 * donuts_per_dozen + donuts_per_half_dozen  # Chris buys 2 and a half dozen donuts
    eaten_donuts = total_donuts * 0.1  # Chris eats 10% of the donuts while driving
    remaining_donuts = total_donuts - eaten_donuts  # Chris has some donuts left when he arrives at work
    remaining_donuts -= 4  # Chris takes 4 donuts for his afternoon snack
    result = remaining_donuts
    return result

print(solution())