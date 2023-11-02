def solution():
    salem_size = 15
    leesburg_size = 1
    leesburg_population = 58940
    salem_population = leesburg_population * salem_size
    out_migration = 130000
    salem_population_after_out_migration = salem_population - out_migration
    women_proportion = 0.5
    salem_women = salem_population_after_out_migration * women_proportion
    result = salem_women
    return result

print(solution())