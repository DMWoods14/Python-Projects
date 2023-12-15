import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from matplotlib.backends.backend_pdf import PdfPages
from tabulate import tabulate

# File path to the CSV containing the air quality data
csv_file_path = 'C:\\Users\\***\\Documents\\School\\Data Sets\\modified_c4_epa_air_quality.csv'

# Read the data from the CSV file into a pandas DataFrame
data = pd.read_csv(csv_file_path)

# Create a PDF file to store the plots and results
pdf_file_path = 'C:\\Users\\***\\Documents\\School\\Data Sets\\PDFs\\EPA_Air_Quality.pdf'
pdf_pages = PdfPages(pdf_file_path)

# Plot a histogram of the 'aqi_log' column and save it to the PDF
plt.figure()
data["aqi_log"].hist()
plt.title('Histogram of aqi_log (Central Tendency)')
plt.xlabel('AQI Log Values')
plt.ylabel('Frequency')
pdf_pages.savefig()
plt.close()

# Calculate mean and standard deviation for further analysis
mean_aqi_log = data["aqi_log"].mean()
std_aqi_log = data["aqi_log"].std()

def get_top_rows_closest_to_limit(data, limit, n=5):
    # Calculate the absolute difference from the limit and select the top n rows
    sorted_rows = data.loc[data["aqi_log"].sub(limit).abs().sort_values().head(n).index]
    return tabulate(sorted_rows, headers='keys', tablefmt='grid') + '\n'

# Check 1st empirical rule (68% of the aqi_log data falls within 1 standard deviation of the mean)
lower_limit_1st_rule = round(mean_aqi_log - 1 * std_aqi_log, 2)
upper_limit_1st_rule = round(mean_aqi_log + 1 * std_aqi_log, 2)
    output_text_1 = f"The 1st Lower limit is: {lower_limit_1st_rule} and the 1st Upper limit is: {upper_limit_1st_rule}\n"
    output_text_1 += "\n"  # Add a newline for spacing
    output_text_1 += "Top 5 rows closest to the Lower Limit:\n"
    output_text_1 += get_top_rows_closest_to_limit(data, lower_limit_1st_rule)
    output_text_1 += "\n"  # Add a newline for spacing
    output_text_1 += "Top 5 rows closest to the Upper Limit:\n"
    output_text_1 += get_top_rows_closest_to_limit(data, upper_limit_1st_rule)

# Save the results to the PDF without graph background
plt.figure(figsize=(16, 5))
plt.axis('off')
plt.text(0, 1.1, output_text_1, fontsize=8, family='monospace', verticalalignment='top')
pdf_pages.savefig()
plt.close()

# Check 2nd empirical rule (95% of the aqi_log data falls within 2 standard deviations of the mean)
lower_limit_2nd_rule = round(mean_aqi_log - 2 * std_aqi_log, 2)
upper_limit_2nd_rule = round(mean_aqi_log + 2 * std_aqi_log, 2)
    output_text_2 = f"The 2nd Lower limit is: {lower_limit_2nd_rule} and the 2nd Upper limit is: {upper_limit_2nd_rule}\n"
    output_text_2 += "\n"  # Add a newline for spacing
    output_text_2 += "Top 5 rows closest to the Lower Limit:\n"
    output_text_2 += get_top_rows_closest_to_limit(data, lower_limit_2nd_rule)
    output_text_2 += "\n"  # Add a newline for spacing
    output_text_2 += "Top 5 rows closest to the Upper Limit:\n"
    output_text_2 += get_top_rows_closest_to_limit(data, upper_limit_2nd_rule)

# Save the results to the PDF without graph background
plt.figure(figsize=(16, 5))
plt.axis('off')
plt.text(0, 1.1, output_text_2, fontsize=8, family='monospace', verticalalignment='top')
pdf_pages.savefig()
plt.close()

# Check 3rd empirical rule (99.7% of the aqi_log data falls within 3 standard deviations of the mean)
lower_limit_3rd_rule = round(mean_aqi_log - 3 * std_aqi_log, 2)
upper_limit_3rd_rule = round(mean_aqi_log + 3 * std_aqi_log, 2)
    output_text_3 = f"The 3rd Lower limit is: {lower_limit_3rd_rule} and the 3rd Upper limit is: {upper_limit_3rd_rule}\n"
    output_text_3 += "\n"  # Add a newline for spacing
    output_text_3 += "Top 5 rows closest to the Lower Limit:\n"
    output_text_3 += get_top_rows_closest_to_limit(data, lower_limit_3rd_rule)
    output_text_3 += "\n"  # Add a newline for spacing
    output_text_3 += "Top 5 rows closest to the Upper Limit:\n"
    output_text_3 += get_top_rows_closest_to_limit(data, upper_limit_3rd_rule)

# Save the results to the PDF without graph background
plt.figure(figsize=(16, 5))
plt.axis('off')
plt.text(0, 1.1, output_text_3, fontsize=8, family='monospace', verticalalignment='top')
pdf_pages.savefig()
plt.close()

# Calculate z-scores for the 'aqi_log' column
data["z_score"] = stats.zscore(data["aqi_log"], ddof=1)  # ddof=degrees of freedom correction (sample vs. population)

# Filter data based on z-scores
outliers = data[(data["z_score"] > 3) | (data["z_score"] < -3)]

# Save the results to the PDF without graph background
plt.figure(figsize=(13, 1))
plt.axis('off')
    output_text_outliers = "Rows with z-scores greater than 3 or less than -3:\n" + tabulate(outliers.head(5), headers='keys', tablefmt='grid') + '\n'
plt.text(0, 1.1, output_text_outliers, fontsize=8, family='monospace', verticalalignment='top')
pdf_pages.savefig()
plt.close()

# Close the PDF
pdf_pages.close()
