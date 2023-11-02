import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
   
def load_file(in_file):
    all_score = []
    with open(in_file, "r") as f:
        data = f.readlines()
        for i in data:
            score = i.split()[-1]
            all_score.append(score)
            
    return all_score

def plot_histplot(in_csv, save_dir=None):
    sns.set_theme(style="darkgrid")
    
    in_data = pd.read_csv(in_csv, sep="\t")
    now_key = in_data.columns.tolist()
    # assert key == now_key.strip()
    # all_score = np.array(load_file(in_csv))[1:]
    # print(in_data.iloc[1])
    # print(in_data[key][10].split()[-1])
    # sns.displot(all_score, kde=True, bins=20)
    for key in now_key:
        if "ID" in key:
            continue
        save_file = save_dir + "{}_score.png".format(key.strip())
        # sns.kdeplot(in_data[key], fill=True, linestyle='solid', color='green')
        sns.displot(in_data[key], kde=True, bins=20)
        xlabel = "{} score".format(key.strip())
        # if xlabel is not None:
        plt.xlabel(xlabel)  
        plt.show()
        plt.savefig(save_file, dpi=300, bbox_inches="tight")
    
def plot_boxplot(in_csv, key=None, save_file=None,):
    
    # sns.set_theme(style="whitegrid")
    sns.set_theme(style="darkgrid", font_scale=2)

        
    in_data = pd.read_csv(in_csv, sep="\t")
    now_key = in_data.columns.tolist()
    in_data = in_data.drop(['discourse_representation', 'coherence_step_vs_step'], axis=1)

    # mean and std error
    col_mean = in_data.mean().iloc[1:]
    col_std = in_data.std().iloc[1:]
    
    
    ax = sns.barplot(x=col_mean.values, y=col_mean.index, yerr=col_std.values, 
                errorbar="sd",
                # capsize=10, 
                orient='h')
    
    # 去掉左边的刻度
    ax.set_yticks([])
    # sns.barplot(x=new_data.index, y='mean', data=new_data, yerr='std', capsize=0.1)
    # plt.errorbar(x=col_mean.index, y=col_mean.values, yerr=col_std.values, fmt='none', capsize=10)
    
    # Plot the orbital period with horizontal boxes
    
    plt.show()
    plt.savefig(save_file, dpi=300, bbox_inches="tight")
    
if __name__ == '__main__':
    # in_file = "plots/code_length.csv"

    # plot hitplot
    # in_dir = "metric/results/roscoe-512-roberta-base-6/"
    # in_file = in_dir + "scores_recor.tsv"

    # plot_histplot(in_file, save_dir=in_dir)
    
    
    # plot Horizontal boxplot
    num = 8
    in_file = "metric/results/metric_for_all_data/roscoe-512-roberta-base-{}/scores_recor.tsv".format(num)
    save_image = "metric/results/metric_for_all_data/roscoe-512-roberta-base-{}/score_4_index.png".format(num)
    plot_boxplot(in_file, save_file=save_image)
    
    # 
    # plot_histplot("metric/results_for_enhanced_data/fathiful.tsv", save_dir="metric/results_for_enhanced_data/")