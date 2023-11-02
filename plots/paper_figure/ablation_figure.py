import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def line_plot(data, save_file, top_y=None):
    sns.set_theme(style="whitegrid", font_scale=1.7)
    # sns.set_theme(style="white")
    # sns.set_theme(style="darkgrid")

    data = pd.DataFrame(data)
    g = sns.relplot(
    # g = sns.relplot(
                x="Model Scale",
                y="Sove Rate (%)",
                style="Training",
                hue="Training",
                data=data, 
                kind="line",
                # kind="reg",
                markers=True, 
                dashes=False,
                # linewidth=2,
                # size="size",
                # sizes={1:in_size, 2:in_size, 3:in_size, 4:in_size, 5:in_size, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2}
                # palette="tab10", linewidth=2.5
                # sizes=[1000]  # 设置标记的大小为 50
                # s=5000  # 设置标记的大小为 50
                # scale=1.5,
                )
    if top_y is not None:
        plt.axhline(y=top_y, color='red', linestyle='--', label='codex')
    # plt.legend()
    # 获取FacetGrid对象的轴，并设置x轴的刻度和标签
    # ax = g.axes[0, 0]
    # ax.set_xticks(data["Frac. data kept"].unique())
    # ax.set_xticklabels(data["Frac. data kept"].unique())
    # 遍历每一个 AxesSubplot 对象，并添加我们自己的散点图
    # for training, subset in data.groupby("Training"):
    #     for ax in g.axes.flat:
    #         ax.scatter(subset["Model Scale"], subset["Sove Rate (%)"], s=100)
    
    plt.savefig(save_file, dpi=500, bbox_inches="tight")
    
def scatter_plot(data, save_file, top_y=None):
    sns.set_theme(style="whitegrid", font_scale=1.7)
    data = pd.DataFrame(data)
    plt.figure() 
    # 使用 scatterplot 绘制散点图
    g = sns.scatterplot(
        x="Model Scale",
        y="Sove Rate (%)",
        hue="Training",
        style="Training",
        data=data,
        markers=True,
        s=100,  # 设置散点的大小为 100
    )
    
    # 使用 lineplot 在同一 Axes 上添加线条
    sns.lineplot(
        x="Model Scale",
        y="Sove Rate (%)",
        hue="Training",
        style="Training",
        data=data, 
        dashes=False,
        linewidth=3,
        ax=g,  # 指定 Axes 对象
        )
    g.legend().remove()
    # # 获取已有的图例句柄和标签
    # handles, labels = g.get_legend_handles_labels()

    # # 获取类别的数量
    # n = len(data['Training'].unique())

    # # 将对应的句柄组合成元组，并传递给 plt.legend() 函数
    # plt.legend(handles=[(h1, h2) for h1, h2 in zip(handles[:n], handles[n:])],
    #         labels=labels[n:],
    #         bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
    # 移动图例
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.savefig(save_file, dpi=500, bbox_inches="tight")

def nested_barplot(data, save_file, top_y=None):
    # sns.color_palette("flare")
    sns.set_theme(style="whitegrid", font_scale=1.7, palette="pastel")
    
    data = pd.DataFrame(data)
    plt.figure()
    g = sns.catplot(
    data=data, 
    kind="bar",
    x="Model Scale", 
    y="Sove Rate (%)", 
    hue="Training",
    # errorbar="sd", 
    palette="dark", 
    alpha=.6, 
    height=6
    )
    g.despine(left=True)
    # g.set_axis_labels("", "Sove Rate (%)")
    # g.legend.set_title("")
    
    #  # 去掉y轴标签
    g.set_axis_labels("Model Scale", "")
    
    # # 去掉图例
    # g.legend.remove()
    
    plt.savefig(save_file, dpi=500, bbox_inches="tight")
    


if __name__ == '__main__':
    
    # samll GSM8K
    data = {
        "Training": [
                    "Base Model", "Base Model", "Base Model",
                    "Fine-Tune", "Fine-Tune", "Fine-Tune",
                    "PaD", "PaD", "PaD",
                    "w/ Self-Distillation", "w/ Self-Distillation", "w/ Self-Distillation", 
                    "w/ Verification", "w/ Verification", "w/ Verification", 
                    ],
        "Sove Rate (%)": [ 
                        1.06, 0.76, 2.96,
                        3.8, 6.3, 7.5,
                        30.64, 34.37, 36.04,
                        27.22, 36.34, 39.23,
                        31.17, 39.31, 44.18,
                        ],
        
        "Model Scale": [
                        "0.06B", "0.22B", "0.77B",
                        "0.06B", "0.22B", "0.77B",
                        "0.06B", "0.22B", "0.77B",
                        "0.06B", "0.22B", "0.77B",
                        "0.06B", "0.22B", "0.77B",
                            ],
    }
    
    # scatter_plot(data, "plots/paper_figure/ablation/gsm8k_ablation.png", 
    #         #   top_y=19.7
    #           )
    nested_barplot(data, "plots/paper_figure/ablation/gsm8k_ablation.png", 
            #   top_y=19.7
              )


    # ASDiv
    data["Sove Rate (%)"] = [ 
                        0.28, 0.19, 3.62,
                        4.1, 5.5, 10.1,
                        44.43, 49.30, 50.45,
                        44.39, 48.97, 51.16,
                        45.15, 51.02, 52.36,
                        ]
    nested_barplot(data, "plots/paper_figure/ablation/ASDiv_ablation.png", 
            #   top_y=74.0
              )
    
    # SVAMP
    
    data["Sove Rate (%)"] = [ 
                            0.2, 0.0, 0.0, 
                            3.0, 5.8, 7.2,
                            35.1, 45.0, 47.2,
                            37, 43.2, 48.2,
                            38.5, 43.2, 50.2,
                            ]
    nested_barplot(data, "plots/paper_figure/ablation/SVAMP_ablation.png", 
            #   top_y=69.9
              )
    
    # MathiArith
    data["Sove Rate (%)"] = [ 
            0.6, 0.0, 0.0, 
            4.5, 11.6, 22.8,
            60.83, 70.17, 75.66,
            66.83, 71.83, 79.16,
            73.5, 82.33, 80.83,
            ]
    nested_barplot(data, "plots/paper_figure/ablation/MathiArith_ablation.png", 
            #   top_y=44.0
              )
    
    # BBH
    data["Sove Rate (%)"] = [ 
            12.0, 10.18, 28.09,
            3.2, 3.8, 1.12,
            1.78, 1.44, 1.78,
            1.30, 2.0, 1.9,
            1.76, 2.09, 2.06
            ]
    nested_barplot(data, "plots/paper_figure/ablation/bbh_ablation.png", 
            #   top_y=56.0
              )