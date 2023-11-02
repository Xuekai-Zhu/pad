def solution():
    """Daniel owns a textile company. Every Monday he delivers 20 yards of fabric, and every Tuesday he delivers twice the amount of fabric he delivers on Monday. Every Wednesday, he delivers 1/4 of the amount of fabric he delivers on Tuesday. If each yard of fabric costs $2 and each yard of yarn costs $3, how much does he earn from Monday to Wednesday?"""
    fabric_price = 2
    yarn_price = 3
    monday_delivery = 20
    tuesday_delivery = 2 * monday_delivery
    wednesday_delivery = tuesday_delivery / 4
    total_fabric_delivery = monday_delivery + tuesday_delivery + wednesday_delivery
    fabric_earnings = total_fabric_delivery * fabric_price
    yarn_earnings = 0 # unclear how much yarn is sold or at what price
    total_earnings = fabric_earnings + yarn_earnings
    result = total_earnings
    return result

print(solution())