import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_histplot(in_csv, key=None, save_file=None, xlabel=None):
    # 设置Seaborn的风格和调色板
    sns.set_theme(style="darkgrid")
    
    in_data = pd.read_csv(in_csv)
    # print(in_data)
    
    sns.displot(in_data[key], kde=True, bins=20)
    if xlabel is not None:
        plt.xlabel(xlabel)
    plt.show()
    plt.savefig(save_file, dpi=300, 
                # bbox_inches="tight"
                )
    
if __name__ == '__main__':
    # in_file = "plots/code_length.csv"
    in_file = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/code_length.csv"
    plot_histplot(in_file, key="inputs_length", save_file="dataset/gsm8k-generat-data/enhanced_data/7_time_data/input_lengths.png", xlabel="Question Length")
    plot_histplot(in_file, key="code_length", save_file="dataset/gsm8k-generat-data/enhanced_data/7_time_data/code_lengths.png", xlabel="Code Length")
    
    