def solution():
    sales_fabric = 36 / 3  # A third of the sales are in the fabric section
    sales_jewelry = 36 / 4  # A quarter of the sales are in the jewelry section
    sales_stationery = 36 - sales_fabric - sales_jewelry  # The rest of the sales are in the stationery section
    result = sales_stationery
    return result

print(solution())