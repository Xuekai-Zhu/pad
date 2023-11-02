def solution():
     
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