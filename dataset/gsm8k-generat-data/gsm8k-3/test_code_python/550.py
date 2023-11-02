def solution():
    """Randy had $3,000. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. What was the value, in dollars, of the rest?"""
    # Define the amount Randy had initially and the amount Smith gave him
    randy_initial = 3000
    smith_gift = 200

    # Calculate the amount Randy had after Smith's gift
    randy_total = randy_initial + smith_gift

    # Calculate the amount Randy gave to Sally
    randy_spent = 1200

    # Calculate the amount Randy kept for himself
    randy_rest = randy_total - randy_spent

    # Display the value of the rest
    result = randy_rest
    return result

print(solution())