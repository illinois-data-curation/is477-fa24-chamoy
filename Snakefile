rule all:
    input:
        "visualizations/heatmap.png",
        "visualizations/barchart.png"

rule generate_heatmap:
    input:
        "output/cleaned_enriched_gene_expression.csv"
    output:
        "visualizations/heatmap.png"
    script:
        "scripts/heatmap.py"

rule generate_barchart:
    input:
        "output/cleaned_enriched_gene_expression.csv"
    output:
        "visualizations/barchart.png"
    script:
        "scripts/barchart.py"
