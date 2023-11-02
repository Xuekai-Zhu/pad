def solution():
    num_bottles_A = 300
    price_A = 4.0

    num_bottles_B = 350
    price_B = 3.5

    # Calculate the total revenue of Company A and Company B
    revenue_A = num_bottles_A * price_A
    revenue_B = num_bottles_B * price_B

    # Calculate the difference in revenue between the two companies
    difference = abs(revenue_A - revenue_B)
    result = difference
    return result

print(solution())