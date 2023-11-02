def solution():
     basket_a = 4
     basket_b = 6
     basket_c = 3
     color_a = "red"
     color_b = "yellow"
     color_c = "white"
     color_d = "green"
     diff_1 = abs(basket_a - basket_b)
     diff_2 = abs(basket_a - basket_c)
     diff_3 = abs(basket_b - basket_c)
     if diff_1 >= diff_2 and diff_1 >= diff_3:
         result = diff_1
     elif diff_2 >= diff_1 and diff_2 >= diff_3:
         result = diff_2
     else:
         result = diff_3
     return result
     
Question: 64三角形顶点坐标如下:(0,0),(8,0),(4,7)，求其面积?
答案：

def solution():
    x1

print(solution())