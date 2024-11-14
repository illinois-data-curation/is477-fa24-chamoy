**Status Report**

Our project aims to analyze gene expression profiles across various cancer types to identify unique patterns that can be used to classify and predict cancer types accurately. By integrating gene expression data with clinical labels specific to cancer types, we hope to uncover biomarkers or gene signatures that are unique to each cancer type. This research could have significant applications in early cancer diagnosis, personalized treatment strategies, and overall improvement in patient outcomes. The project is grounded in a primary research question: "How do gene expression profiles differ across various cancer types, and can these differences be used to accurately classify and predict cancer types?"
Our team consists of Faith Chow and Kayla Moy, both acting as data scientists and researchers on the project. We are working with two main datasets: a JSON file containing patient demographic data and a CSV file with gene expression data for various cancer types. The JSON file follows the mCODE standard, enabling interoperability across healthcare systems and standardizing cancer patient data. The CSV file, on the other hand, provides RNA sequencing data for each sample, with gene expression values associated with specific cancer types such as BRCA (breast cancer), LUAD (lung adenocarcinoma), PRAD (prostate cancer), and KIRC (kidney renal clear cell carcinoma). These datasets serve as the foundation for our analysis, with the JSON providing contextual patient data and the CSV enabling high-dimensional gene expression analysis.

**Progress on Project Tasks**
Since the project’s commencement, we have progressed through foundational tasks, including dataset integration, version control, data profiling, cleaning, and exploratory analysis, each building toward reliable insights on cancer-related gene expression. From November 1-6, we focused on integrating the gene_expression.csv dataset using Python and Pandas, ensuring each cancer type was labeled accurately and tracked with GitHub version control for collaborative progress and documentation. Between November 7-9, we imputed missing values, normalized gene distributions, and applied log-transformations to improve data normality, documenting each step for reproducibility. On November 10-12, we initiated exploratory data analysis with key visualizations: a heatmap displaying average gene expression by cancer type provided insight into expression variations, while a stacked bar chart showed the distribution of cancer-related data elements across categories like Identifiers, Demographics, and Treatment Plans. These visualizations, stored in results/initial_analysis_plots/, revealed early clustering patterns suggesting potential biomarkers, as detailed in results/initial_findings.md. Finally, on November 13-14, we compiled a status report to summarize our findings and invite peer feedback.

**Updated Timeline**
As of this status report, we have kept to our original timeline. Below is an updated timeline indicating completed tasks and upcoming milestones:
Date            Task            Status          Expected Completion
Nov 1-3  Dataset Integration    Complete        Nov 3
Nov 4-6     Version Control     Complete        Nov 6
Nov 7-9     Data Cleaning       Complete        Nov 9
Nov 10-12   DA & Visual         Complete        Nov 12
Nov 13-14   Status Report       In Progress     Nov 14
Nov 16-18   Data Profile&Model  Pending         Nov 18
Nov 19-21   Advanced Viz&Analysis Pending       Nov 21
Nov 22-24   Dev. for Reprod.    Pending         Nov 24
Nov 25-27   Automated Workflow  Pending         Nov 27
Nov 28-31   Integrate Results   Pending         Nov 30
Dec 1-11    Final Report        Pending         Dec 11

This timeline reflects our progress so far, with the initial phases of data integration, cleaning, and exploratory analysis completed. Our next steps involve model development, where we will build both supervised and unsupervised models to classify cancer types based on gene expression profiles. After model development, we will focus on comparative analysis, refining our visualizations, and creating a reproducible package for our analysis. Our goal is to complete all analyses and documentation by the project’s December 11 deadline.

**Changes to the Project Plan**
Based on initial results, we made several adjustments. First, we expanded data cleaning with added log-transformations to address unexpected skewness in gene distributions and ensure data quality. Next, we extended the exploratory analysis to gain a more detailed understanding of gene expression patterns across cancer types. This additional step provided valuable insights that will guide the feature selection and model development phases. Finally, we decided to incorporate peer feedback by sharing our status report with colleagues and advisors, whose input will refine our approach to feature selection and analysis for greater relevance and accuracy in future steps.

**Evidence of Progress**
Our progress is documented through various artifacts committed to the GitHub repository, which demonstrates the work completed so far. These artifacts include:
**Data Integration and Cleaning:**
- gene_expression.csv: The main dataset, prepared for analysis.
- cleaned_gene_expression.csv and cleaned_cancer_patient.json: Scripts for data integration and cleaning, tracking each step for reproducibility.
**Data Visualization:**
- eda.ipynb: Contains our python data script in cleaning the original data sets (CSV and JSON) and the appropriate visualizations for each data set. 

**Next Steps**
Our upcoming tasks, aligned with the revised project timeline, will guide us toward completing a robust, reproducible analysis pipeline for cancer gene expression data. From November 16-18, we will conduct additional data profiling and initiate model development, building both supervised models (e.g., random forests, support vector machines) and unsupervised clustering models to classify cancer types. This phase will include hyperparameter tuning and evaluating performance metrics, such as accuracy and recall, to optimize our models. From November 19-21, we will apply dimensionality reduction techniques like PCA and t-SNE, creating advanced visualizations to capture the high-dimensional structure of gene expression data and clarify separations between cancer types. These visualizations, combined with comparative model analysis, will help identify distinct patterns across cancer types. On November 22-24, we will develop a reproducible package with all code, documentation, and essential functions, ensuring that our analysis is accessible and easily replicable for future research. This will be followed by setting up an automated workflow from November 25-27, which will streamline data processing, model training, and visualization, allowing seamless updates and reapplication of our methods to new datasets. In the final integration phase from November 28-30, we will compile all findings, models, and visualizations into a comprehensive comparative analysis report documenting our process and insights. Finally, from December 1-11, we will complete the final report, which will incorporate all methodologies, analyses, visualizations, and conclusions, ultimately contributing valuable insights into gene-specific expression patterns relevant to cancer diagnosis and treatment. This plan will ensure a complete and reproducible analysis pipeline for advancing cancer research.
