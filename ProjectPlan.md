**Overview**
The goal of this project is to analyze gene expression profiles across various cancer types to identify unique expression patterns that could aid in accurately classifying and predicting cancer types. By integrating gene expression data with clinical cancer type labels, the project aims to discover biomarkers or gene signatures specific to each cancer type. This research could enhance early cancer diagnosis, improve personalized treatment strategies, and potentially contribute to better patient outcomes.

**Research Questions**
How do gene expression profiles differ across various cancer types, and can these differences be used to accurately classify and predict cancer types?

**Team**
Faith Chow: Data Scientist & Researcher
Kayla Moy: Data Scientist & Researcher 

**Datasets**

**Cancer Patient JSON**
link: https://build.fhir.org/ig/HL7/fhir-mCODE-ig/StructureDefinition-mcode-cancer-patient.profile.json.html

The provided JSON file is an electronic health record file between different healthcare systems (FHIRR) for a "Cancer Patient" profile, designed to standardize and facilitate interoperability in recording cancer patient data. This structure, part of the mCODE (Minimal Common Oncology Data Elements) initiative, extends the core FHIR patient profile to support the specific needs of oncology, including additional demographic details like birth sex, race, and ethnicity, alongside mandatory fields like patient status (deceased or alive). These details are critical for organizing and sharing standardized cancer data across healthcare systems.

With the research question, “How do gene expression profiles differ across various cancer types, and can these differences be used to accurately classify and predict cancer type?” this structure supports the foundational data needed to identify and analyze cancer patients by cancer type. Although the profile doesn’t directly contain gene expression data, it has a framework for managing patient-specific information critical for cancer classification and prediction models.

By extending this profile with links to genomic and molecular data, researchers can connect a patient’s clinical information to gene expression profiles, providing context for meaningful cross-analysis across cancer types. For instance, demographic data (such as race, birth sex, and ethnicity) and survival outcomes can contextualize how gene expression varies not only by cancer type but also by these factors. Furthermore, the profile’s structured format makes integrating cancer-specific attributes with gene expression data easier, creating a unified dataset that could be used to train machine learning models for classification and prediction.

This StructureDefinition enables healthcare providers and researchers to collect consistent cancer patient data, forming a standardized dataset that can be expanded with gene expression profiles to support accurate cancer classification and predictive modeling.

**Gene Expression CSV**
link: https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq

The gene expression CSV dataset consists of RNA sequencing data across multiple cancer patient samples. Each row represents a unique patient sample with a labeled cancer type in the first column, such as "BRCA" (breast cancer), "LUAD" (lung adenocarcinoma), "PRAD" (prostate cancer), and "KIRC" (kidney renal clear cell carcinoma). The subsequent columns correspond to specific genes, labeled sequentially as gene_0, gene_1, gene_2, and so on, totaling 2000 gene expression values per sample.

Each entry in this dataset reflects the expression level of a given gene for a particular sample, measured in quantitative values that indicate gene activity. For example, high expression levels in certain genes across specific cancer types could reveal patterns associated with that cancer, potentially serving as biomarkers. This dataset, therefore, provides a comprehensive matrix of gene activity across various cancer types, enabling a comparative analysis of gene expression profiles.

The structure of this dataset is particularly suited for high-dimensional data analysis, such as clustering, feature selection, and supervised machine learning models aimed at cancer classification. By examining differences in gene expression across cancer types, this dataset can reveal distinctive expression patterns or gene signatures associated with each cancer type. Such insights are valuable for understanding the molecular underpinnings of different cancers, potentially guiding personalized treatment approaches or aiding in early diagnosis through gene expression-based classification.

**Timeline**

**November 15 Deadline: Status Report on Preliminary Analysis:**

November 1-3:
- Dataset Integration: Begin by loading and exploring the gene expression CSV file. Use Python/Pandas and/or SQL to integrate multiple cancer datasets, ensuring each cancer type (e.g., BRCA, LUAD, PRAD, KIRC) is properly labeled and distinct.
- Data Structuring: Verify that each sample row has a unique identifier, and each gene column is consistently labeled across samples. Check for consistency in formatting, especially in gene naming and cancer type labels.
- Version Control Setup: Initiate a Git repository to track changes in the dataset and code, ensuring all integration steps are documented.

November 4-6:
- Data Profiling and Assessment: Perform transparent data profiling by examining each gene’s range, distribution, and variance. Check for missing values, outliers, or unusual patterns within each cancer type. Assess data completeness for each gene across samples, flagging any with extensive missing values.
- Quality Assessment: Document any inconsistencies or potential issues found during profiling, such as outlier samples or highly skewed genes. Record findings in a profiling report, outlining areas requiring cleaning and adjustments.

November 7-9:
- Data Cleaning: Based on the profiling report, perform cleaning tasks. This might include imputing missing values with median/mean values, removing low-quality samples, and transforming gene expression values to normalize distributions (e.g., log-transforming if necessary).
- Documentation: Create a log of data cleaning steps, including any parameters used for imputing or transforming data. Make this log accessible in a README file within the project’s repository.

November 10-12:
- Initial Data Analysis and Visualization: Begin exploratory analysis by visualizing high-level patterns in the dataset. Implement clustering techniques (e.g., k-means or hierarchical clustering) to see if samples naturally group by cancer type based on gene expression.
- Visualization Techniques: Generate visualizations like heatmaps for gene expression levels, box plots for major gene groups, and scatter plots to identify any notable separation between cancer types.
- Preliminary Findings: Document initial observations in a draft report, noting any clustering patterns, differences in gene expression by cancer type, or any genes that stand out as potential biomarkers.

November 13-14:
- Status Report Compilation: Summarize all findings in a status report. Include sections on data integration, quality assessment, cleaning processes, initial analysis, and visualization outputs. Highlight early insights into gene expression differences across cancer types and propose next steps for in-depth analysis.
- Feedback Collection: If possible, share the status report with peers or advisors to gather feedback on preliminary findings and proposed methodologies.

**December 1 Deadline: Comparative Analysis Completion**

November 16-18:
- Model Development - Classification and Clustering: Start building machine learning models for cancer type classification. Implement supervised models (e.g., random forests, SVM) to predict cancer types based on gene expression profiles and unsupervised models (e.g., k-means clustering) to observe natural groupings.
- Hyperparameter Tuning: Experiment with different parameters and evaluate model performance metrics (accuracy, precision, recall) to identify the best settings for each model.

November 19-21:
- Advanced Visualization: Develop more refined visualizations to compare gene expression patterns across cancer types. Create PCA (Principal Component Analysis) or t-SNE plots to reduce dimensionality and observe group separations in a visual form.
- Comparative Analysis by Gene: Analyze individual gene contributions by calculating feature importance or examining correlation matrices. Identify key genes that are predictive for specific cancer types.
- Result Documentation: Document results of each model and visualization in a comparative analysis report, highlighting which genes or clusters are significant for cancer classification.

November 22-24:
- Package Development for Reproducibility: Compile the data cleaning, analysis, and model scripts into a reproducible package using Python. Ensure code modularity and add documentation for each function to facilitate understanding and reuse.
- Testing the Package: Run the entire analysis workflow end-to-end on a sample subset to verify the reproducibility of results. Update documentation with any insights gained during testing.

November 25-27:
- Automated Workflow Setup: Use a tool like Jupyter Notebook or Apache Airflow to automate the data analysis pipeline from loading the dataset to producing final results. Ensure the automation handles all data loading, cleaning, analysis, and visualization steps without manual intervention.
- Testing and Debugging: Execute the workflow multiple times with different subsets of data to test its robustness and fix any bugs in the automation process.

November 28-30:
- Integration of All Results: Bring together all findings and insights, focusing on gene expression patterns that distinguish each cancer type. Prepare visual and quantitative summaries of model performance, highlighting classification accuracy and identifying the most predictive genes.
- Finalize Comparative Analysis Report: Complete a detailed comparative analysis report, which will include model details, visualization outputs, and a summary of key findings related to gene expression profiles and cancer classification.

**December 11 Deadline: Final Project Report and Submission**

December 2-4:
- Data and Software Citation: Gather citation details for all datasets, software tools, and libraries used in the project. Ensure that each dataset (e.g., gene expression CSV) and each tool (e.g., Pandas, sklearn) has an accurate and consistent citation format.
- Methodology Documentation: Write a detailed methodology section for the final report, explaining all steps taken from data integration through to model analysis and workflow automation.

December 5-6:
- Metadata Creation: Develop comprehensive metadata for the package, detailing variable descriptions, data sources, analysis methods, and software dependencies. Use a structured format like JSON or Markdown for easy integration with repository documentation.
- Repository Setup: Organize the project files in a structured folder within a repository (e.g., GitHub or Zenodo), including code, data, and documentation. Ensure all files are well-labeled and accessible.

December 7-8:
- Repository Archiving and Persistent Identifier Creation: Archive the project repository on a platform that provides persistent identifiers (e.g., Zenodo or Figshare). Obtain a DOI (Digital Object Identifier) or similar identifier to ensure long-term access and referencability.
- Project Accessibility: Make sure the repository settings allow for open access, with clear instructions for future users on how to replicate the analysis and use the package.

December 9-10:
- Final Project Report Compilation: Draft the final project report, synthesizing all components: data integration, quality assessment, analysis methods, model results, and workflow automation. Emphasize findings on gene-specific expression patterns, cancer classification accuracy, and predictive power of gene expression profiles.
- Recommendations and Applications: Conclude with recommendations for how these findings could support early cancer diagnosis, personalized treatment approaches, or further gene-based cancer research.

December 11:
- Project Submission: Submit the final report, project package, and repository link with DOI. Ensure that all documentation, citations, and metadata are complete and accessible, enabling future researchers to reproduce and build upon this work


