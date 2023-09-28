# Helper Functions 

# Imports 
import matplotlib.pyplot as plt 
import seaborn as sns


# Bar Plot
def b_plot(df, x, y):
    # Create a barplot using Seaborn
    plt.figure(figsize=(6, 6))
    sns.barplot(x=x, y=y, data=df, palette='cool')
    plt.title('Average Age by Squad')
    plt.xlabel('Squad')
    plt.ylabel('Average Age')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()