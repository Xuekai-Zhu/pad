def solution():
    salary = 7000
    num_red_sold = 2
    num_green_sold = 3
    percent_red = 10
    percent_green = 20
    price_red = 20000
    price_green = (salary - (num_red_sold * price_red * (percent_red / 100))) / (num_green_sold * (percent_green / 100))
    result = price_green
    
    return result

print(solution())