def solution():
    """A laboratory has 22 beakers of liquid in a fume hood, and 8 of the beakers have copper ions in them. Adding three drops of a solution will turn the liquid in a beaker blue if there are copper ions present. If the beakers are tested one by one for copper ions and 45 drops are used before all 8 beakers with copper ions are found, how many beakers without copper ions were tested?"""
    total_beakers = 22
    beakers_with_copper = 8
    beakers_without_copper = total_beakers - beakers_with_copper
    tests_per_beaker = 3
    total_tests = tests_per_beaker * beakers_with_copper
    remaining_tests = 45 - total_tests
    beakers_tested_without_copper = remaining_tests / tests_per_beaker
    result = beakers_tested_without_copper
    
    return result

print(solution())