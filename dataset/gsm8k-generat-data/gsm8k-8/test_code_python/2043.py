def solution():
    # Calculate the number of books Brad read last month
    brad_last_month = 6 * 3

    # Calculate the total number of books Brad has read
    brad_total = brad_last_month + 8

    # Calculate the total number of books William has read
    william_total = 6 + (2 * 8)

    if william_total > brad_total:
        result = "William has read more by " + str(william_total - brad_total) + " books"
    else:
        result = "Brad has read more by " + str(brad_total - william_total) + " books"
    return result

print(solution())