import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Plotting:

    def __init__(self):
        pass

    def draw_plots(self, data):
        # Convert the JSON data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Create a folder to store the plots
        os.makedirs("plots", exist_ok=True)

        # Draw the plots
        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x="mean", bins=10)
        plt.savefig("plots/mean.png")

        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x="max", bins=10)
        plt.savefig("plots/max.png")

        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x="min", bins=10)
        plt.savefig("plots/min.png")
        
        plt.figure(figsize=(8, 6))
        plt.hist([df["gt_corners"], df["rb_corners"]], bins=range(15), label=['Ground Truth', 'Predicted'])
        plt.xlabel('Number of corners')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig("plots/histogram.png")
        

        # Return the paths to the saved plots
        return ["plots/mean.png", "plots/max.png", "plots/min.png", "plots/histogram.png"]
