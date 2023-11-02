import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def barplot(in_data, save_file):
    sns.set_theme(style="darkgrid")
    # plt.figure(figsize=(12, 6))
    ax = sns.barplot(y="model", x="Solve Rate (%)", data=in_data,
                # label="model"
                hue="model",
                # width=2.0
                )
    # plt.xticks([])
    # Get the legend handles and labels from the ax object
    handles, labels = ax.get_legend_handles_labels()
    
    # Remove the existing legend
    ax.get_legend().remove()
    ax = sns.barplot(y="model", x="Solve Rate (%)", data=in_data,
                # label="model"
                # hue="model",
                # width=2.0
                )
    plt.legend(handles, labels, title='model', bbox_to_anchor=(0, 1.25, 1, 0.2), loc='upper left')

    # plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=3.)
    plt.xlabel("Math Words Problems Solving Rate (%)")
    # plt.xlabel("Math Word Reasoning (GSM8K)")
    plt.savefig(save_file, dpi=500, bbox_inches="tight")
    
    
if __name__ == '__main__':
    
    data = {
        "model": ["PaLM 540B", "LLaMA 13B", "T5_small 60M", "T5_base 220M", "T5_large 770M"],
        "Solve Rate (%)": [18, 17.8, 27.22, 36.34, 39.23],
        # "PaLM 540B": [18],
        # "LLaMA 13B": [17.8],
        # "T5_small 60M": [27.22],
        # "T5_base 220M": [36.34],
    }
    df = pd.DataFrame(data)
    barplot(data, "comparative_pair.png")