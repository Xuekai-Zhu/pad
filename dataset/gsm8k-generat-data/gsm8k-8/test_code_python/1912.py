def solution():
    # Each truck can carry a maximum load of 2000 pounds
    # Let's assume we fill each truck with only 40-pound boxes
    # Then each truck can carry 50 boxes (2000/40)
    # But the customer has ordered equal quantities of both 10-pound and 40-pound boxes
    # So we need to adjust the number of boxes accordingly

    # Let's say we fill x trucks with 40-pound boxes and y trucks with 10-pound boxes
    # Then we have the following equations:
    # 40 * 50 * x + 10 * 50 * y <= 2000 * 3
    # x + y = 3

    # Solving these equations, we get:
    # x = 2, y = 1
    # So we can ship 100 40-pound boxes and 50 10-pound boxes in each delivery
    # Or we can ship a total of 150 boxes in each delivery (half 40-pound and half 10-pound)

    result = 150
    return result

print(solution())