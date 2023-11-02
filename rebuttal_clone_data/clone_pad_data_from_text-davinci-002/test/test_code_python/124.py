def solution():
    
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