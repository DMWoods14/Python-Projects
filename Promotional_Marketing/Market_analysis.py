import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm
# from statsmodels.graphics.gofplots import qqplot

csv_file_path = 'C:\\Users\\***\\Documents\\School\\Data Sets\\marketing_sales_data.csv'

data = pd.read_csv(csv_file_path)
data = data.dropna(axis=0)
data = data.rename(columns={'Social Media': 'Social_Media'})

ols_formula = 'Sales ~ C(TV) + Radio'
OLS = ols(formula=ols_formula, data=data)

model = OLS.fit()
model_results = model.summary()

# Specify the directory and file paths for the PDF and TXT
pdf_directory = 'C:\\Users\\***\\Documents\\School\\Data Sets\\PDFs'
pdf_file_path = os.path.join(pdf_directory, 'marketing_sales_data.pdf')
txt_file_path = os.path.join(pdf_directory, 'marketing_sales_data_txt.txt')

# Create a PDF file and a TXT file
with PdfPages(pdf_file_path) as pdf, open(txt_file_path, 'w') as txt_file:
    # Scatter plot of Radio and Sales
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=data['Radio'], y=data['Sales'])
    plt.title("Scatter Plot of Radio Advertising and Sales")
    plt.xlabel("Radio Advertising (in units)")
    plt.ylabel("Sales (in units)")
    sns.regplot(x=data['Radio'], y=data['Sales'], ci=None, line_kws={'color': 'red'})
    pdf.savefig()
    plt.close()

    # Scatter plot of Social Media and Sales
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=data['Social_Media'], y=data['Sales'])
    plt.title("Scatter Plot of Social Media Advertising and Sales")
    plt.xlabel("Social Media Advertising (in units)")
    plt.ylabel("Sales (in units)")
    sns.regplot(x=data['Social_Media'], y=data['Sales'], ci=None, line_kws={'color': 'red'})
    pdf.savefig()
    plt.close()

    # Histogram of Residuals
    plt.figure(figsize=(10, 5))
    sns.histplot(model.resid)
    plt.title("Histogram of Residuals")
    plt.xlabel("Residual Value")
    plt.ylabel("Frequency")
    pdf.savefig()
    plt.close()

    # QQ Plot of Residuals
    plt.figure(figsize=(10, 5))
    sm.qqplot(model.resid, line='s')
    plt.title("Normal QQ Plot of Residuals")
    pdf.savefig()
    plt.close()

    # Fitted Values vs Residuals
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=model.fittedvalues, y=model.resid)
    plt.title("Fitted Values vs Residuals")
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.axhline(0, color='red', linestyle='--')
    pdf.savefig()
    plt.close()

    # Save OLS Regression Results to TXT
    results_text = f"\nOLS Regression Results:\n\n{model_results}"
    txt_file.write(results_text)

print(f"Plots saved to: {pdf_file_path}")
print(f"Results saved to: {txt_file_path}")
