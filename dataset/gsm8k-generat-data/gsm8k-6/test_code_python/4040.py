def solution():
    # Calculate the number of cookies left after the adults eat 1/3 of them
    cookies_left = (2/3) * 120  # 1/3 of the cookies are eaten by the adults

    # Calculate the number of cookies each child gets
    cookies_per_child = cookies_left / 4  # the remaining cookies are divided equally among the 4 children
    result = cookies_per_child
    return result

print(solution())