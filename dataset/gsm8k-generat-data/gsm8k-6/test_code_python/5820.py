def solution():
    # Calculate the total number of bonnets made by Mrs. Young
    total_bonnets = 10 + 2 * 10 + 5 + (5 - 5)  # on Tues+Wed, she made twice more than Mon (2*10); on Thurs, made 5 more than Mon; on Fri, made 5 less than Thurs
    bonnets_per_orphanage = total_bonnets / 5  # divide the total number of bonnets evenly to 5 orphanages
    result = bonnets_per_orphanage
    return result

print(solution())