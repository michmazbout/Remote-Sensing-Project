import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming your data is in two CSV files named 'file1.csv' and 'file2.csv'
file1_path = 'C:/Users/Elias/Desktop/New folder/Altech_V3.csv'
file2_path = 'C:/Users/Elias/Desktop/New folder/Altech_LAND7.csv'

# Read the data from both files into separate DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Concatenate the two DataFrames along the rows (axis=0)
df = pd.concat([df1, df2], ignore_index=True)

# Extract the year from the 'date' column and create a new column 'year'
# Convert the 'date' column to datetime format with the specified format
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = df['date'].dt.year
df['area_km'] = df['area'] * 30 * 30 / 1000000

# Calculate the average area for each year
average_area_per_year = df.groupby('year')['area_km'].mean().reset_index()

# Fit a polynomial curve (you may need to adjust the degree based on your data)
coefficients = np.polyfit(average_area_per_year['year'], average_area_per_year['area_km'], 2)
fitted_curve = np.polyval(coefficients, average_area_per_year['year'])

# Find the first and last Y values
first_y_value = average_area_per_year['area_km'].iloc[0]
last_y_value = average_area_per_year['area_km'].iloc[-1]

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.plot(average_area_per_year['year'], average_area_per_year['area_km'], color='blue', label='Average Area')
plt.plot(average_area_per_year['year'], fitted_curve, color='red', label='Fitted Curve')

# Annotate the plot with the first and last Y values
plt.annotate(f'First Y: {first_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[0], first_y_value),
             xytext=(0, -60), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))
plt.annotate(f'Last Y: {last_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[-1], last_y_value),
             xytext=(-110, 10), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))

# Uncomment the equation label and add it to the plot
#equation_label = f'Fitted Curve: {coefficients[0]:.2e}x^2 + {coefficients[1]:.2e}x + {coefficients[2]:.2e}'
#plt.text(0.3, 0.2, equation_label, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.title('Aletsch Glacier\'s Average Surface Area per Year')
plt.xlabel('Year')
plt.ylabel('Average Yearly Area (km^2)')
# Set x-ticks to display every 2 years
plt.xticks(average_area_per_year['year'][::2], rotation=45, ha="right")
plt.legend()

# Save the plot as a high-resolution PDF
plt.savefig('Aletsch Glacier .pdf', format='pdf', dpi=1200)
plt.show()

# Assuming your data is in two CSV files named 'file1.csv' and 'file2.csv'
file1_path = 'C:/Users/Elias/Desktop/New folder/Pasterze_L5.csv'
file2_path = 'C:/Users/Elias/Desktop/New folder/Pasterze_L7.csv'

# Read the data from both files into separate DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Concatenate the two DataFrames along the rows (axis=0)
df = pd.concat([df1, df2], ignore_index=True)

# Extract the year from the 'date' column and create a new column 'year'
# Convert the 'date' column to datetime format with the specified format
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = df['date'].dt.year
df['area_km'] = df['area'] * 30 * 30 / 1000000

# Calculate the average area for each year
average_area_per_year = df.groupby('year')['area_km'].mean().reset_index()

# Fit a polynomial curve (you may need to adjust the degree based on your data)
coefficients = np.polyfit(average_area_per_year['year'], average_area_per_year['area_km'], 2)
fitted_curve = np.polyval(coefficients, average_area_per_year['year'])

# Find the first and last Y values
first_y_value = average_area_per_year['area_km'].iloc[0]
last_y_value = average_area_per_year['area_km'].iloc[-1]

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.plot(average_area_per_year['year'], average_area_per_year['area_km'], color='blue', label='Average Area')
plt.plot(average_area_per_year['year'], fitted_curve, color='red', label='Fitted Curve')

# Annotate the plot with the first and last Y values
plt.annotate(f'First Y: {first_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[0], first_y_value),
             xytext=(40, 60), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))
plt.annotate(f'Last Y: {last_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[-1], last_y_value),
             xytext=(-110, -20), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))

# Uncomment the equation label and add it to the plot
#equation_label = f'Fitted Curve: {coefficients[0]:.2e}x^2 + {coefficients[1]:.2e}x + {coefficients[2]:.2e}'
#plt.text(0.3, 0.2, equation_label, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.title('Pasterze Glacier\'s Average Surface Area per Year')
plt.xlabel('Year')
plt.ylabel('Average Yearly Area (km^2)')
# Set x-ticks to display every 2 years
plt.xticks(average_area_per_year['year'][::2], rotation=45, ha="right")

plt.legend()

# Save the plot as a high-resolution PDF
plt.savefig('Pasterze Glacier .pdf', format='pdf', dpi=1200)
plt.show()


# Assuming your data is in two CSV files named 'file1.csv' and 'file2.csv'
file1_path = 'C:/Users/Elias/Desktop/New folder/Mer_de_Glace_L5.csv'
file2_path = 'C:/Users/Elias/Desktop/New folder/Mer_de_Glace_L7.csv'

# Read the data from both files into separate DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Concatenate the two DataFrames along the rows (axis=0)
df = pd.concat([df1, df2], ignore_index=True)

# Extract the year from the 'date' column and create a new column 'year'
# Convert the 'date' column to datetime format with the specified format
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = df['date'].dt.year
df['area_km'] = df['area'] * 30 * 30 / 1000000

# Calculate the average area for each year
average_area_per_year = df.groupby('year')['area_km'].mean().reset_index()

# Fit a polynomial curve (you may need to adjust the degree based on your data)
coefficients = np.polyfit(average_area_per_year['year'], average_area_per_year['area_km'], 2)
fitted_curve = np.polyval(coefficients, average_area_per_year['year'])

# Find the first and last Y values
first_y_value = average_area_per_year['area_km'].iloc[0]
last_y_value = average_area_per_year['area_km'].iloc[-1]

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.plot(average_area_per_year['year'], average_area_per_year['area_km'], color='blue', label='Average Area')
plt.plot(average_area_per_year['year'], fitted_curve, color='red', label='Fitted Curve')

# Annotate the plot with the first and last Y values
plt.annotate(f'First Y: {first_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[0], first_y_value),
             xytext=(50, -10), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))
plt.annotate(f'Last Y: {last_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[-1], last_y_value),
             xytext=(-90, 100), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))

# Uncomment the equation label and add it to the plot
#equation_label = f'Fitted Curve: {coefficients[0]:.2e}x^2 + {coefficients[1]:.2e}x + {coefficients[2]:.2e}'
#plt.text(0.3, 0.2, equation_label, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.title('Mer de Glace Glacier\'s Average Surface Area per Year')
plt.xlabel('Year')
plt.ylabel('Average Yearly Area (km^2)')
# Set x-ticks to display every 2 years
plt.xticks(average_area_per_year['year'][::2], rotation=45, ha="right")
plt.legend()

# Save the plot as a high-resolution PDF
plt.savefig('Mer de Glace Glacier.pdf', format='pdf', dpi=1200)
plt.show()


# Assuming your data is in two CSV files named 'file1.csv' and 'file2.csv'
file1_path = 'C:/Users/Elias/Desktop/New folder/Findelin_L5.csv'
file2_path = 'C:/Users/Elias/Desktop/New folder/Findelin_L7.csv'

# Read the data from both files into separate DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Concatenate the two DataFrames along the rows (axis=0)
df = pd.concat([df1, df2], ignore_index=True)

# Extract the year from the 'date' column and create a new column 'year'
# Convert the 'date' column to datetime format with the specified format
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = df['date'].dt.year
df['area_km'] = df['area'] * 30 * 30 / 1000000

# Calculate the average area for each year
average_area_per_year = df.groupby('year')['area_km'].mean().reset_index()

# Fit a polynomial curve (you may need to adjust the degree based on your data)
coefficients = np.polyfit(average_area_per_year['year'], average_area_per_year['area_km'], 2)
fitted_curve = np.polyval(coefficients, average_area_per_year['year'])

# Find the first and last Y values
first_y_value = average_area_per_year['area_km'].iloc[0]
last_y_value = average_area_per_year['area_km'].iloc[-1]

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.plot(average_area_per_year['year'], average_area_per_year['area_km'], color='blue', label='Average Area')
plt.plot(average_area_per_year['year'], fitted_curve, color='red', label='Fitted Curve')

# Annotate the plot with the first and last Y values
plt.annotate(f'First Y: {first_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[0], first_y_value),
             xytext=(00, 60), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))
plt.annotate(f'Last Y: {last_y_value:.2f} km^2', xy=(average_area_per_year['year'].iloc[-1], last_y_value),
             xytext=(-110, 10), textcoords='offset points', arrowprops=dict(arrowstyle="->", color='black'))

# Uncomment the equation label and add it to the plot
#equation_label = f'Fitted Curve: {coefficients[0]:.2e}x^2 + {coefficients[1]:.2e}x + {coefficients[2]:.2e}'
#plt.text(0.3, 0.2, equation_label, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

plt.title('Findel Glacier\'s Average Surface Area per Year')
plt.xlabel('Year')
plt.ylabel('Average Yearly Area (km^2)')
# Set x-ticks to display every 2 years
plt.xticks(average_area_per_year['year'][::2], rotation=45, ha="right")
plt.legend()

# Save the plot as a high-resolution PDF
plt.savefig('Findel Glacier .pdf', format='pdf', dpi=1200)
plt.show()
