def solution():
    sandra_money = 10
    mother_money = 4
    father_money = mother_money * 2

    candy_price = 0.5
    jelly_bean_price = 0.2

    num_candies = 14
    num_jelly_beans = 20

    # Calculate total amount of money Sandra has
    total_money = sandra_money + mother_money + father_money

    # Calculate total cost of candies and jelly beans
    total_cost = (num_candies * candy_price) + (num_jelly_beans * jelly_bean_price)

    # Calculate how much money Sandra will be left with
    left_money = total_money - total_cost
    result = left_money
    return result

print(solution())