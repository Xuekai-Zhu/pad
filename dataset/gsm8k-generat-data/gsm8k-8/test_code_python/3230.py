def solution():
    # Calculate the number of giraffe statues that can be made with the total jade
    num_giraffes = 1920 // 120

    # Calculate the total profit from selling giraffe statues
    giraffe_profit = num_giraffes * 150

    # Calculate the amount of jade used for one elephant statue
    elephant_jade = 2 * 120

    # Calculate the maximum number of elephant statues that can be made with the total jade
    max_num_elephants = 1920 // elephant_jade

    # Calculate the total profit from selling elephant statues
    elephant_profit = max_num_elephants * 350

    # Calculate the difference in profit between selling only giraffe statues and selling only elephant statues
    difference = elephant_profit - giraffe_profit

    result = difference
    return result

print(solution())