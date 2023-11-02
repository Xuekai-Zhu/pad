def solution():
    """Great Grandma Jones has three children. And each of her children has three children of their own, who are Great Grandma Jones' grandchildren. And each of these grandchildren has three babies of their own, who are Great Grandma Jones' great grand-babies. If all of the family show up at the family reunion, how many great grand-babies will be there for Great Grandma Jones to kiss?"""
    children = 3
    grandchildren_per_child = 3
    great_grandbabies_per_grandchild = 3
    total_great_grandbabies = (children * grandchildren_per_child) * (grandchildren_per_child * great_grandbabies_per_grandchild)
    result = total_great_grandbabies
    return result

print(solution())