# Stacked Bar Chart Visualization for Key Cancer-Related Categories
import numpy as np
import matplotlib.pyplot as plt

file_path = '/Users/kaylamoy/Desktop/is477-fa24-chamoy/CSV/cleaned_gene_expression.csv'
data = pd.read_csv('output/cleaned_enriched_gene_expression.csv')
data.head()

category_data = {
    "Identifiers": [10, 5, 3],        
    "Demographics": [7, 4, 6],         
    "Clinical Observations": [15, 8, 10],  
    "Treatment Plans": [10, 12, 8],   
    "Follow-Up": [5, 3, 6]            
}

categories = list(category_data.keys())
counts = np.array(list(category_data.values()))
subcategories = ["Type1", "Type2", "Type3"] 

fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(categories))

for idx, subcategory in enumerate(subcategories):
    ax.bar(categories, counts[:, idx], label=subcategory, bottom=bottom)
    bottom += counts[:, idx]

ax.set_title("Distribution of Cancer-Related Data Elements by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Number of Elements")
ax.legend(title="Subcategories")
plt.xticks(rotation=45)
plt.show()
plt.savefig("visualizations/barchart.png")