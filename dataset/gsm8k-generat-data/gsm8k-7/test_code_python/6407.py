def solution():
    total_chocolates = 50
    num_caramels = 3
    num_nougats = 2 * num_caramels
    num_truffles = num_caramels + 6
    num_peanut_clusters = total_chocolates - num_caramels - num_nougats - num_truffles

    # Calculate the percentage chance of picking a peanut cluster
    percentage_peanut_clusters = (num_peanut_clusters / total_chocolates) * 100
    result = percentage_peanut_clusters
    return result

print(solution())