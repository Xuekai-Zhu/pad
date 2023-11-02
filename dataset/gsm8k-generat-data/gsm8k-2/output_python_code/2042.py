def solution():
    """William read 6 books last month and Brad read thrice as many books as William did. This month, in an effort to catch up, Williams read twice as much as Brad, who read 8 books. Who has read more across the two months, and by how much?"""
    william_last_month = 6
    brad_last_month = 3 * william_last_month
    brad_this_month = 8
    william_this_month = 2 * brad_this_month
    total_william = william_last_month + william_this_month
    total_brad = brad_last_month + brad_this_month
    if total_william > total_brad:
        result = "William has read more by " + str(total_william - total_brad) + " books."
    elif total_brad > total_william:
        result = "Brad has read more by " + str(total_brad - total_william) + " books."
    else:
        result = "They have read the same number of books."
    return result

print(solution())