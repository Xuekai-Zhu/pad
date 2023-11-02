def solution():
    rock_cd_price = 5
    pop_cd_price = 10
    dance_cd_price = 3
    country_cd_price = 7
    num_cds_per_genre = 4
    total_budget = 75

    # Calculate the total cost of all rock CDs
    total_rock_cd_cost = rock_cd_price * num_cds_per_genre

    # Calculate the total cost of all pop CDs
    total_pop_cd_cost = pop_cd_price * num_cds_per_genre

    # Calculate the total cost of all dance CDs
    total_dance_cd_cost = dance_cd_price * num_cds_per_genre

    # Calculate the total cost of all country CDs
    total_country_cd_cost = country_cd_price * num_cds_per_genre

    # Calculate the total cost of all CDs
    total_cd_cost = total_rock_cd_cost + total_pop_cd_cost + total_dance_cd_cost + total_country_cd_cost

    # Calculate how much money Julia is short
    amount_short = total_cd_cost - total_budget
    result = amount_short
    return result

print(solution())