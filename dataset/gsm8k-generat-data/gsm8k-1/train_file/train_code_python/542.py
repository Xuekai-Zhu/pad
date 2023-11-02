def solution():
    """In Mary's class, there are 25 students. Their teacher told them they could pay $50 each to finance a big science project that they and their society would benefit greatly from. They all paid the full amount except for 4 students, who paid half. How much was the class able to gather together?"""
    num_students = 25
    full_payment = 50
    half_payment = full_payment / 2
    num_full_payments = num_students - 4
    total_paid = (num_full_payments * full_payment) + (4 * half_payment)
    result = total_paid
    return result

print(solution())