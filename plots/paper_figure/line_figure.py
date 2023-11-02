import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def line_plot(data, save_file, top_y=None):
    # sns.set_theme(style="whitegrid")
    # sns.set_theme(style="white")
    # sns.set_theme(style="darkgrid")
    sns.set_theme(style="whitegrid", font_scale=1.1)

    data = pd.DataFrame(data)
    g = sns.relplot(
                x="Frac. data kept",
                y="Solve Rate (%)",
                style="pruning",
                hue="pruning",
                data=data, 
                kind="line",
                # kind="reg",
                markers=True, 
                dashes=False,
                # palette="tab10", linewidth=2.5
                )
    if top_y is not None:
        plt.axhline(y=top_y, color='gray', linestyle='--', label='no_pruning')
    # plt.legend()
    # 获取FacetGrid对象的轴，并设置x轴的刻度和标签
    ax = g.axes[0, 0]
    ax.set_xticks(data["Frac. data kept"].unique())
    ax.set_xticklabels(data["Frac. data kept"].unique())
    
    plt.savefig(save_file, dpi=500, bbox_inches="tight")
    
    
def line_correct_plot(data, save_file, top_y=None):
    sns.set_theme(style="whitegrid", font_scale=1.1)
    # sns.set_theme(style="white")
    # sns.set_theme(style="darkgrid")

    data = pd.DataFrame(data)
    g = sns.relplot(
                x="Frac. data kept",
                y="Grammatically Correct Rate (%)",
                style="Model Scale",
                hue="Model Scale",
                data=data, 
                kind="line",
                # kind="reg",
                markers=True, 
                dashes=False,
                # palette="tab10", linewidth=2.5
                )
    
    plt.axhline(y=top_y, color='gray', linestyle='--')
    # plt.legend()
    # 获取FacetGrid对象的轴，并设置x轴的刻度和标签
    ax = g.axes[0, 0]
    ax.set_xticks(data["Frac. data kept"].unique())
    ax.set_xticklabels(data["Frac. data kept"].unique())
    plt.legend(loc='lower right')
    plt.savefig(save_file, dpi=500, bbox_inches="tight")
    
    
    
if __name__ == '__main__':
    
    # samll model data
    data = {
        "pruning": [
                    # "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning","no_pruning",
                    # "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate" ,"compressed_rate", "compressed_rate", 
                    "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful",
                    "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd",
                    "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy",
                    ],
        "Solve Rate (%)": [ 
                        # 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64,
                        # 30.64, 28.36, 26.69, 25.01, 24.03, 22.50, 21.74, 19.01, 11.02, 8.82,
                        30.64, 27.75, 25.62, 22.66, 24.03, 22.50, 18.93, 17.41, 13.99, 9.04,
                        30.64, 24.94, 25.09, 24.33, 21.36, 22.28, 22.66, 16.73, 15.51, 8.51,
                        30.64, 25.93, 26.00, 24.48, 23.04, 22.28, 19.08, 15.89, 11.78, 7.68,
                        ],
        
        "Frac. data kept": [
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            ],
    }
    # 
    # line_plot(data, "plots/paper_figure/data_pruning_figure/small_model_pruning_line_plot.png", 
    #           top_y=30.64
    #           )
    
    
    # base model data
    data = {
        "pruning": [
                    # "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning","no_pruning",
                    # "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate", "compressed_rate" ,"compressed_rate", "compressed_rate", 
                    "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful", "faithful",
                    "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd",
                    "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy",
                    ],
        "Solve Rate (%)": [ 
                        # 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64,
                        # 34.37, 34.44, 33.91, 32.54, 30.26, 27.30, 25.55, 21.06, 20.6, 10.11,
                        34.37, 34.60, 32.39, 31.25, 28.28, 26.99, 25.32, 22.12, 17.79, 11.55,
                        34.37, 33.30, 30.79, 29.42, 28.74, 24.79, 24.48, 21.82, 18.93, 13.23,
                        34.37, 33.46, 30.57, 30.41, 29.35, 26.53, 24.33, 19.46, 16.19, 7.98,
                        ],
        
        "Frac. data kept": [
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            ],
    }
    
    # line_plot(data, "plots/paper_figure/data_pruning_figure/base_model_pruning_line_plot.png", top_y=34.37)


    # base model data
    data = {
        "Model Scale": [
                    # "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning", "no_pruning","no_pruning",
                    "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M", "CodeT5_base 220M",
                    "CodeT5_small 60M", "CodeT5_small 60M", "CodeT5_small 60M", "CodeT5_small 60M", "CodeT5_small 60M", "CodeT5_small 60M", "CodeT5_small 60M", "CodeT5_small 60M" ,"CodeT5_small 60M", "CodeT5_small 60M", 
                    # "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd", "GraNd",
                    # "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy", "entropy",
                    ],
        "Grammatically Correct Rate (%)": [ 
                        # 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64,
                        90.49, 90.19, 90.79, 88.51, 88.89, 90.57, 87.60, 83.34, 85.32, 82.73,
                        89.80, 86.08, 86.76, 85.17, 85.32, 83.65, 84.10, 83.95, 79.84, 74.52,
                        # 34.37, 33.30, 30.79, 29.42, 28.74, 24.79, 24.48, 21.82, 18.93, 13.23,
                        # 34.37, 33.46, 30.57, 30.41, 29.35, 26.53, 24.33, 19.46, 16.19, 7.98,
                        ],
        
        "Frac. data kept": [
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 
                            1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            # 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1,
                            ],
    }
    
    line_correct_plot(data, "plots/paper_figure/gramatica_correct/gredint_Grammatically_Correct_line_plot.png", top_y=89.9)
    
    # base model data 
    data["Grammatically Correct Rate (%)"] = [ 
                        # 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64,
                        90.49, 93.38, 94.98, 90.87, 89.88, 94.60, 91.78, 94.82, 91.78, 89.50,
                        89.80, 91.55, 91.25, 91.63, 94.31, 90.57, 91.25, 89.65, 88.44, 86.99,
                        # 34.37, 33.30, 30.79, 29.42, 28.74, 24.79, 24.48, 21.82, 18.93, 13.23,
                        # 34.37, 33.46, 30.57, 30.41, 29.35, 26.53, 24.33, 19.46, 16.19, 7.98,
                        ]
    # line_correct_plot(data, "plots/paper_figure/gramatica_correct/fathiful_Grammatically_Correct_line_plot.png", top_y=89.9)
    
    
    # base model data 
    data["Grammatically Correct Rate (%)"] = [ 
                        # 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64, 30.64,
                        90.49, 96.19, 91.93, 91.55, 96.12, 94.14, 94.22, 92.92, 94.60, 91.25,
                        89.80, 87.14, 89.58, 89.20, 89.58, 90.57, 89.80, 92.31, 91.02, 91.71,
                        # 34.37, 33.30, 30.79, 29.42, 28.74, 24.79, 24.48, 21.82, 18.93, 13.23,
                        # 34.37, 33.46, 30.57, 30.41, 29.35, 26.53, 24.33, 19.46, 16.19, 7.98,
                        ]
    # line_correct_plot(data, "plots/paper_figure/gramatica_correct/entropy_Grammatically_Correct_line_plot.png", top_y=89.9)