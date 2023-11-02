def solution():
    giraffe_jade = 120
    giraffe_price = 150
    elephant_jade = giraffe_jade * 2
    elephant_price = 350
    total_jade = 1920

    # Calculate the maximum number of giraffes Nancy can make
    num_giraffes = total_jade // giraffe_jade

    # Calculate the maximum number of elephants Nancy can make
    num_elephants = total_jade // elephant_jade

    # Calculate the total amount of money Nancy can make with giraffes
    total_giraffe_money = num_giraffes * giraffe_price

    # Calculate the total amount of money Nancy can make with elephants
    total_elephant_money = num_elephants * elephant_price

    # Calculate the difference in money by making elephants instead of giraffes
    money_difference = total_elephant_money - total_giraffe_money
    result = money_difference
    return result

print(solution())