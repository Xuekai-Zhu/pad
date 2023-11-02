def solution():
    # Calculate the amount of fabric delivered on each day
    monday_delivery = 20
    tuesday_delivery = monday_delivery * 2
    wednesday_delivery = tuesday_delivery / 4

    # Calculate the total amount of fabric delivered from Monday to Wednesday
    total_delivery = monday_delivery + tuesday_delivery + wednesday_delivery

    # Calculate the total earnings from the fabric deliveries
    fabric_earnings = total_delivery * 2

    # Assume Daniel also sells yarn and calculate the earnings from that
    yarn_earnings = 0

    # Calculate the total earnings
    total_earnings = fabric_earnings + yarn_earnings
    result = total_earnings
    return result

print(solution())