import matplotlib.pyplot as plt
import seaborn as sns


def plot_pie(sizes, labels, save):
    sns.set_theme(style="darkgrid", font_scale=1.5)
    # 创建数据集
    sizes = sizes
    labels = labels
    colors = ['#808080', '#696969', '#778899']
    # colors = ['red', 'orange', 'yellow',]
    plt.figure()
    # 绘制扇形图
    plt.pie(sizes, labels=labels, 
            colors=colors,
            autopct='%1.1f%%')

    # 添加标题
    # plt.title('Training data')

    # 显示图形
    plt.show()
    plt.savefig(save, dpi=300, bbox_inches="tight")
    
if __name__ == '__main__':
    # plot chatgpt train dataset output
    sizes = [1 - 0.9809, 0.9809 - 0.7735, 0.7735]
    labels = ["Compilation Error", "Miscalculation", "Success"]
    plot_pie(sizes, labels, "plots/paper_figure/chat_eval /train_set_eval.png")
    
    # plot chatgpt test dataset output
    sizes = [1 - 0.8987, 0.8987 - 0.7285, 0.7285]
    labels = ["Compilation Error", "Miscalculation", "Success"]
    plot_pie(sizes, labels, "plots/paper_figure/chat_eval /test_set_eval.png")
    
    
    
    