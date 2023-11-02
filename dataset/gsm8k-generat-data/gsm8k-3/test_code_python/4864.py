def solution():
    """Martha is knitting winter clothes for her 3 grandchildren, who are all the same size (identical triplets.) Each set of clothes consists of a woolen hat, a scarf, a sweater, a pair of mittens, and a pair of wooly socks. She can knit a hat in 2 hours. A scarf takes her 3 hours. Each mitten takes her about an hour to knit. A sock takes an hour and a half. Each sweater takes her 6 hours. How long will it take her to knit all the outfits?"""
    
    # Define the time it takes to knit each item
    hat_time = 2
    scarf_time = 3
    mitten_time = 1
    sock_time = 1.5
    sweater_time = 6
    
    # Define the number of items per outfit
    hat_num = 1
    scarf_num = 1
    mitten_num = 2
    sock_num = 2
    sweater_num = 1
    
    # Define the number of grandchildren
    num_grandchildren = 3
    
    # Calculate the total time to knit all outfits
    total_time = (hat_time + scarf_time + (mitten_time * mitten_num) + (sock_time * sock_num) + sweater_time) * hat_num * scarf_num * mitten_num * sock_num * sweater_num * num_grandchildren
    
    # Display the total time
    result = total_time
    return result

print(solution())