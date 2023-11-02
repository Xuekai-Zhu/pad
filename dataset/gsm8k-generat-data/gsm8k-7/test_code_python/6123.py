def solution():
    num_red_tractors = 2
    red_tractor_price = 20000

    num_green_tractors = 3
    green_tractor_salary_percentage = 0.2

    total_salary = 7000

    # Calculate the total salary from selling red tractors
    red_tractor_salary = num_red_tractors * (red_tractor_price * 0.1)

    # Calculate the total salary from selling green tractors
    green_tractor_salary = (total_salary - red_tractor_salary) / num_green_tractors

    # Calculate the price of a single green tractor
    green_tractor_price = green_tractor_salary / green_tractor_salary_percentage
    result = green_tractor_price
    return result

print(solution())