def solution():
     """A church has 120 members. 40% are adults. The rest are children. How many children more children are there than adults?"""
     total_members = 120
     percent_adults = 40
     percent_children = 100 - percent_adults
     adults = total_members * (percent_adults / 100)
     children = total_members * (percent_children / 100)
     result = children - adults
     return result

print(solution())