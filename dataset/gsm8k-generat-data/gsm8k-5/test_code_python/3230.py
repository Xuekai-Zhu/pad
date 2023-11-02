def solution():
    # Calculate the number of giraffes Nancy can make with 1920 grams of jade
    num_giraffes = 1920 // 120

    # Calculate the total revenue Nancy would make from selling only giraffes
    revenue_giraffes = num_giraffes * 150

    # Calculate the amount of jade required for one elephant
    jade_per_elephant = 2 * 120

    # Calculate the maximum number of elephants Nancy can make with 1920 grams of jade
    max_num_elephants = 1920 // jade_per_elephant

    # Calculate the total revenue Nancy would make from selling only elephants
    revenue_elephants = max_num_elephants * 350

    # Calculate the additional revenue Nancy would make by turning all the jade into elephants instead of giraffes
    additional_revenue = revenue_elephants - revenue_giraffes
    result = additional_revenue
    return result

print(solution())