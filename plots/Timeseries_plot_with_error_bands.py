import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Code Source : https://seaborn.pydata.org/examples/errorband_lineplots.html

sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
# fmri = sns.load_dataset("plots/results_0216.csv")
fmri = pd.read_csv("results_0216.csv")

# Plot the responses for different events and regions
sns.barplot(x="Instruction Tuning",
              y="Test Solve Rate (%)",
            #  hue="Instruction Tuning", 
             hue="Interaction", 
            #  style="event",
             data=fmri)
plt.show()
plt.savefig("test.png")