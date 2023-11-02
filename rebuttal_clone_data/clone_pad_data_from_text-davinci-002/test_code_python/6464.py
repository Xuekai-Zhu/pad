def solution():
    mahogany_planted = 50
    narra_planted = 30
    trees_that_fell = 5
    mahogany_that_fell = trees_that_fell - 1
    narra_that_fell = trees_that_fell - mahogany_that_fell
    total_mahogany = mahogany_planted + (mahogany_that_fell * 3)
    total_narra = narra_planted + (narra_that_fell * 2)
    result = total_mahogany + total_narra
    return result

print(solution())