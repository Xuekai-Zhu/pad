def solution():
    """There are many CDs in the store. The rock and roll CDs are $5 each, the pop CDs are $10 each, the dance CDs are $3 each, and the country CDs are $7 each. Julia wants to buy 4 of each, but she only has 75 dollars. How much money is she short?"""
    # Define the prices of each type of CD and the number of CDs needed
    rock_price = 5
    pop_price = 10
    dance_price = 3
    country_price = 7
    cds_needed = 4

    # Calculate the total cost of each type of CD
    rock_cost = rock_price * cds_needed
    pop_cost = pop_price * cds_needed
    dance_cost = dance_price * cds_needed
    country_cost = country_price * cds_needed

    # Calculate the total cost of all CDs
    total_cost = rock_cost + pop_cost + dance_cost + country_cost

    # Calculate the amount of money Julia is short
    money_short = total_cost - 75

    # return the result
    result = money_short
    return result

print(solution())