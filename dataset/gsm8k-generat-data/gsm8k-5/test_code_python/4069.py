def solution():
    meat_weight = 10 * 16  # 10 pounds of meat mix, converted to ounces
    num_links = 40  # 40 sausage links in the string
    meat_per_link = meat_weight / num_links  # Calculate the meat in each link

    # Subtract the meat eaten by Brandy
    meat_remaining = (num_links - 12) * meat_per_link
    result = meat_remaining
    return result

print(solution())