def solution():
    # Calculate the total amount of tomatoes that Tommy bought
    total_tomatoes = 20 * 3  # each crate can hold 20 kilograms of tomatoes and Tommy has 3 crates
    # Calculate the weight of the rotten tomatoes
    rotten_tomatoes = 3
    # Calculate the weight of the good tomatoes
    good_tomatoes = total_tomatoes - rotten_tomatoes
    # Calculate the total revenue from selling the good tomatoes
    revenue = good_tomatoes * 6
    # Calculate the total cost of buying the crates of tomatoes
    cost = 330
    # Calculate Tommy's profit
    profit = revenue - cost
    result = profit
    return result

print(solution())