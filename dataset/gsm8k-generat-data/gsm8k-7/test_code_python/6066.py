def solution():
    num_dark_cds = 2
    dark_cd_price = 2 * 12  # "AVN" CD is half the price of one from "The Dark"
    avn_cd_price = 12
    num_90s_cds = 5

    # Calculate the total cost of CDs by "The Dark"
    total_dark_cost = num_dark_cds * dark_cd_price

    # Calculate the total cost of the "AVN" CD
    total_avn_cost = avn_cd_price

    # Calculate the total cost of the 90s CDs as a percentage of the other CDs' cost
    other_cds_cost = total_dark_cost + total_avn_cost
    ninety_percent_of_cost = 0.4  # 40% of the cost
    total_90s_cost = other_cds_cost * ninety_percent_of_cost

    # Calculate the total cost of all CDs
    total_cost = total_dark_cost + total_avn_cost + total_90s_cost
    result = total_cost
    return result

print(solution())