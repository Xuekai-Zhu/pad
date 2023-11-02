import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_jointplot(save_file_1=None, save_file_2=None, compressed_file=None, gradient_file=None, entropy_file=None, plot_1=False, plot_2=True):
    
    # compressed ratio
    in_data_compressed = pd.read_csv(compressed_file)

    # 设置Seaborn的风格和调色板
    sns.set_theme(style="darkgrid")
    
    if plot_1:
        # gradient
        in_data_gradient = pd.read_csv(gradient_file)
        data_1 = pd.concat([in_data_compressed, in_data_gradient], axis=1)
        # print(data_1)
        # sampled_df = data_1.sample(n=700)
        # data 1 
        keys = data_1.columns.tolist()
        sns.jointplot(x=keys[0], y=keys[1], data=data_1,
                    kind="reg", truncate=False,
                    #   xlim=(0, 60), ylim=(0, 12),
                    color="m", height=7)

        # if xlabel is not None:
        #     plt.xlabel(xlabel)
            
        # plt.show()
        plt.savefig(save_file_1, dpi=300, bbox_inches="tight")
    
    
    if plot_2:
        # entropy
        in_data_entropy = pd.read_csv(entropy_file)
        
        data_2 = pd.concat([in_data_compressed, in_data_entropy], axis=1)
        sampled_df = data_2.sample(n=700)
        # data 2 
        keys = data_2.columns.tolist()
        sns.jointplot(x=keys[0], y=keys[1], data=sampled_df,
                    kind="reg", truncate=False, order=3, 
                    #   xlim=(0, 60), ylim=(0, 12),
                    color="r", height=7)

        # if xlabel is not None:
        #     plt.xlabel(xlabel)
            
        # plt.show()
        plt.savefig(save_file_2, dpi=300, bbox_inches="tight")

def plot_histplot(in_csv, key=None, save_file=None, xlabel=None):
    # 设置Seaborn的风格和调色板
    sns.set_theme(style="darkgrid")
    
    in_data = pd.read_csv(in_csv)
    # print(in_data)
    
    sns.displot(in_data[key], kde=True, bins=20)
    if xlabel is not None:
        plt.xlabel(xlabel)
    plt.show()
    plt.savefig(save_file, dpi=300, bbox_inches="tight")
    
def plot_only_jointplot(save_file=None,file_1=None, file_2=None):
    data_1 = pd.read_csv(file_1)
    data_2 = pd.read_csv(file_2)
    data = pd.concat([data_1, data_2], axis=1)
    # print(data)
    sampled_df = data.sample(n=700)
    # 设置Seaborn的风格和调色板
    sns.set_theme(style="darkgrid")
    keys = data.columns.tolist()
    sns.jointplot(x=keys[0], y=keys[1], data=sampled_df,
                    kind="reg", truncate=False,
                    #   xlim=(0, 60), ylim=(0, 12),
                    color="m", height=7)
    
    plt.savefig(save_file, dpi=300, bbox_inches="tight")

if __name__ == '__main__':
    # plot_jointplot(save_file_1="compressed_code/compressed_gradient.png",
    #                save_file_2="compressed_code/compressed_entropy.png",
    #                compressed_file="compressed_code/results_compressed_ratio.csv",
    #                gradient_file="compressed_code/gradient_v2.csv",
    #                entropy_file="compressed_code/entropy.csv",
    #             #    plot_1=True,
    #                plot_2=True
    #                )
    
    # plot_histplot(in_csv="compressed_code/results.csv", key="compressed_ratio", save_file="ony_compressed.png", xlabel="compressed_ratio")
    plot_only_jointplot("faithful_compressed.png", "compressed_code/results_compressed_ratio.csv", "metric/results_for_enhanced_data/fathiful.tsv")