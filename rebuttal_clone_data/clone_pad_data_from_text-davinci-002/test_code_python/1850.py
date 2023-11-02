def solution():
     lawn_length = 22
     lawn_width = 36
     seed_coverage = 250
     seed_coverage_lawn = (lawn_length * 2) + (lawn_width * 2)
     seed_coverage_leftover = seed_coverage - seed_coverage_lawn
     result = seed_coverage_leftover
     return result

print(solution())