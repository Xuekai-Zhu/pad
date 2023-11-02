def solution():
    """There are 29 pupils in a class. The teacher has 9 coupons; each coupon can be redeemed for 100 bottles of apple juice. The teacher gives each student 2 bottles of apple juice to drink for lunch. After redeeming all her coupons and giving each student their apple juice lunch, how many bottles of apple juice does the teacher have for herself?"""
    num_students = 29
    num_coupons = 9
    bottles_per_coupon = 100
    bottles_per_student = 2
    total_bottles_given = num_students * bottles_per_student
    total_bottles_redeemed = num_coupons * bottles_per_coupon
    remaining_bottles = total_bottles_redeemed - total_bottles_given
    result = remaining_bottles
    return result

print(solution())