def solution():
    flour_per_batch = 2  # 2 pounds of flour per dozen cookies
    bags_of_flour = 4  # 4 bags of flour, each weighing 5 pounds

    # Calculate the total amount of flour in pounds
    total_flour = bags_of_flour * 5

    # Calculate the total number of batches of cookies
    total_batches = total_flour // flour_per_batch

    # Calculate the total number of cookies
    total_cookies = total_batches * 12

    # Calculate the number of cookies left after Jim eats 15
    cookies_left = total_cookies - 15
    result = cookies_left
    return result

print(solution())