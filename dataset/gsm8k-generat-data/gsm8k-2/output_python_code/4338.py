def solution():
    """Matilda bought a smartphone for $300. Then she decided she wouldn't use it anyway and sold it for $255. What percentage of the initial cost did she lose?"""
    initial_cost = 300
    selling_price = 255
    loss = initial_cost - selling_price
    loss_percentage = (loss / initial_cost) * 100
    result = loss_percentage
    return result

print(solution())