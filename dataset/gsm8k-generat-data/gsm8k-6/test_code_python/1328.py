def solution():
    # Calculate the total yards of fabric delivered from Monday to Wednesday
    monday_delivery = 20
    tuesday_delivery = 2 * monday_delivery
    wednesday_delivery = tuesday_delivery * (1/4)
    total_delivery = monday_delivery + tuesday_delivery + wednesday_delivery

    # Calculate the total earnings from fabric and yarn
    fabric_earnings = total_delivery * 2  # each yard of fabric costs $2
    yarn_earnings = 0  # no yarn is delivered
    total_earnings = fabric_earnings + yarn_earnings
    result = total_earnings
    return result

print(solution())