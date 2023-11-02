def solution():
    # Population at the start
    population_start = 100000

    # Increase in population due to birth
    birth_rate = 0.6
    population_birth = population_start * (1 + birth_rate)**10

    # Net increase in population due to migration
    migration_rate = 2500 - 2000  # Net gain of 500 people per year
    population_migration = migration_rate * 10  # 10 years

    # Total population at the end of 10 years
    population_end = population_birth + population_migration
    result = population_end
    return result

print(solution())