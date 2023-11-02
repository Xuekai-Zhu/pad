def solution():
    # Calculate the total number of peanut butter cookies
    total_pb_cookies = 40 + 30  # Jenny brought in 40 pb cookies, Marcus brought in 30 pb cookies

    # Calculate the total number of cookies
    total_cookies = total_pb_cookies + 50 + 20  # 50 chocolate chip cookies, 20 lemon cookies

    # Calculate the probability of Renee picking a peanut butter cookie
    pb_prob = total_pb_cookies / total_cookies

    # Convert the probability to a percentage
    pb_percentage = pb_prob * 100

    result = pb_percentage
    return result

print(solution())