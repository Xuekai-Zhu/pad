def solution():
    """Valerie’s cookie recipe makes 16 dozen cookies and calls for 4 pounds of butter. She only wants to make 4 dozen cookies for the weekend. How many pounds of butter will she need?"""
    dozen_cookies = 16
    butter_per_dozen = 4 / dozen_cookies
    desired_dozen_cookies = 4
    butter_needed = butter_per_dozen * desired_dozen_cookies
    result = butter_needed
    return result

print(solution())