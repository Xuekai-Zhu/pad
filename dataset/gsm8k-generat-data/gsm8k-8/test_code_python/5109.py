def solution():
    # Define the initial production in March
    march_production = 3000

    # Calculate the production in April (double March's production)
    april_production = march_production * 2

    # Calculate the production in May (double April's production)
    may_production = april_production * 2

    # Calculate the production in June (double May's production)
    june_production = may_production * 2

    # Calculate the production in July (double June's production)
    july_production = june_production * 2

    result = july_production
    return result

print(solution())