def solution():
    """Michael is replacing the carpet in his bedroom. The new carpet he's chosen costs $12 per square foot, plus $2 per square foot for padding underneath. His contractor charges $4 per square foot to remove the old carpet,
    and $34 per square foot to install the new carpet. His bedroom measures 18 feet by 12 feet. How much will it cost Michael to replace the carpet?"""
    length = 18
    width = 12
    area = length * width
    carpet_cost = 12
    padding_cost = 2
    removal_cost = 4
    install_cost = 34
    total_cost = (carpet_cost + padding_cost) * area + removal_cost * area + install_cost * area
    
    return total_cost

print(solution())