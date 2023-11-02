def solution():
     """Mr. Lu owns a computer store. For last month, half of their sales are laptops, one-third are netbooks, and the rest are desktop computers. If Mr. Lu's store was able to sell a total of 72 computers, how many of them are desktop computers?"""
     total_computers_sold = 72
     laptop_percentage = 0.5
     netbook_percentage = 0.33
     desktop_percentage = 1 - (laptop_percentage + netbook_percentage)
     laptops_sold = total_computers_sold * laptop_percentage
     netbooks_sold = total_computers_sold * netbook_percentage
     desktop_sold = total_computers_sold * desktop_percentage
     result = desktop_sold
     return result

print(solution())