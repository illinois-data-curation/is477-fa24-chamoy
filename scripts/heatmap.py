import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/kaylamoy/Desktop/is477-fa24-chamoy/CSV/cleaned_gene_expression.csv'
data = pd.read_csv('output/cleaned_enriched_gene_expression.csv')
data.head()

#Heatmap Visualization
missing_values = data.isnull().sum().sum()
cleaned_data = data.dropna() if missing_values > 0 else data

#mean expression levels for each gene grouped by "Class"
mean_expression_per_class = cleaned_data.groupby('Class').mean()

#First 50 genes
subset_genes = mean_expression_per_class.iloc[:, :50]

plt.figure(figsize=(15, 8))
sns.heatmap(subset_genes, cmap="viridis", annot=False)
plt.title("Average Gene Expression by Class (Subset of Genes)")
plt.xlabel("Genes")
plt.ylabel("Class")
plt.show()
plt.savefig("visualizations/heatmap.png")