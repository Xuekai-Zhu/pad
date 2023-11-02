def solution():
Carlos_bought = 50
caramels = 3
nougats = caramels * 2
truffles = caramels + 6
peanut_clusters = Carlos_bought - (caramels + nougats + truffles)
total_chocolates = caramels + nougats + truffles + peanut_clusters
chance_of_peanut_cluster = (peanut_clusters/total_chocolates) * 100
result = chance_of_peanut_cluster

return result

print(solution())