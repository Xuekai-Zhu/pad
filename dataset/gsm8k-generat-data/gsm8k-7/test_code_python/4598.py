def solution():
    num_emp_per_sector = 20

    # Calculate the cost of men's white t-shirts
    men_white_price = 20
    men_black_price = 18

    # Calculate the cost of women's t-shirts based on being cheaper
    women_white_price = men_white_price - 5
    women_black_price = men_black_price - 5

    # Calculate the total cost of men's t-shirts for both sectors
    men_total_cost = (men_white_price + men_black_price) * num_emp_per_sector

    # Calculate the total cost of women's t-shirts for both sectors
    women_total_cost = (women_white_price + women_black_price) * num_emp_per_sector

    # Calculate the total cost of all t-shirts
    total_cost = men_total_cost + women_total_cost
    result = total_cost
    return result

print(solution())