def solution():
    num_caramels = 3  # There are 3 caramels
    num_nougats = 2 * num_caramels  # There are twice as many nougats as caramels
    num_truffles = num_caramels + 6  # There are as many truffles as caramels plus 6
    num_peanut_clusters = 50 - (num_caramels + num_nougats + num_truffles)  # The rest are peanut clusters

    # Calculate the percentage chance that a chocolate picked at random is a peanut cluster
    percent_peanut_clusters = (num_peanut_clusters / 50) * 100
    result = percent_peanut_clusters
    return result

print(solution())