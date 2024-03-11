# Helper Functions

# Imports 
import matplotlib.pyplot as plt 
import seaborn as sns


# Bar Plot
def b_plot(df, x, y):
    # Create a barplot using Seaborn
    plt.figure(figsize=(10, 5))
    sns.barplot(x=x, y=y, data=df, palette='cool')
    plt.title(f'Average {x} by {y}')
    plt.xlabel(f'{y}')
    plt.ylabel(f'Average {y}')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()


# Line Plot 
def l_plot(df, x, y):
    # Create a lineplot using Seaborn
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=x, y=y, data=df, marker='o', color='b', markersize=8, linewidth=2, errorbar='sd')
    plt.title(f'Trend in Average {y} Over Time')
    plt.suptitle("Surrounding Area Represents the Standard Deviation of the Mean")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

# Scatter Plot
def s_plot(df, x, y):
    # Create a scatter plot using Seaborn
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=x, y=y, data=df, color='b', marker='o', s=100)  # Adjust marker and size as needed
    plt.title(f'{y} vs. {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()