def solution():
    # Calculate the number of giraffe statues Nancy can make
    giraffe_jade = 120
    giraffe_num = 1920 // giraffe_jade

    # Calculate the total revenue from giraffe statues
    giraffe_revenue = giraffe_num * 150

    # Calculate the amount of jade needed for one elephant statue
    elephant_jade = 2 * giraffe_jade

    # Calculate the number of elephant statues Nancy can make
    elephant_num = 1920 // elephant_jade

    # Calculate the total revenue from elephant statues
    elephant_revenue = elephant_num * 350

    # Calculate the difference in revenue between elephant and giraffe statues
    revenue_diff = elephant_revenue - giraffe_revenue

    result = revenue_diff
    return result

print(solution())