import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_nested_hist(data, save_file, top_y=None):
    sns.set_theme(style="whitegrid", font_scale=1.7)

    plt.savefig(save_file, dpi=500, bbox_inches="tight")
    data = pd.DataFrame(data)
    plt.figure() 
    
    g = sns.catplot(
    data=data, kind="bar",
    x="species", 
    y="body_mass_g", 
    # hue="sex",
    # errorbar="sd", 
    palette="dark",
    alpha=.6, 
    height=6
    )
    
    
if __name__ == '__main__':
    data = {
        "dataset":["GSM8K", "GSM8K", 
                   "ASDiv",
                   "SVAMP",
                   "MathiArith",
                   "BBH"
                   ]
    }    