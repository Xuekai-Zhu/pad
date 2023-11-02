def solution():
    """Daniel owns a textile company. Every Monday he delivers 20 yards of fabric, and every Tuesday he delivers twice the amount of fabric he delivers on Monday. Every Wednesday, he delivers 1/4 of the amount of fabric he delivers on Tuesday. If each yard of fabric costs $2 and each yard of yarn costs $3, how much does he earn from Monday to Wednesday?"""
    # Define the amount of fabric delivered on each day
    monday = 20
    tuesday = monday * 2
    wednesday = tuesday * 0.25

    # Calculate the total yards of fabric delivered
    total_fabric = monday + tuesday + wednesday

    # Calculate the earnings from the fabric deliveries
    fabric_earnings = total_fabric * 2

    # Calculate the earnings from the yarn deliveries
    yarn_earnings = 0

    # Display the total earnings
    result = fabric_earnings + yarn_earnings
    return result

print(solution())