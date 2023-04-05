import pandas as pd

def process_population_data(filename):

	#Load the data into a Data Frame
	read_input_file = pd.read_csv(filename, skiprows=4)

	#Extract the data for the years 2012 to 2020
	population_years_df = read_input_file.loc[:, 'Country Name':'2020']
	population_years_df.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)

	#Transpose the DataFrame to get a coutry as view
	population_countries_df = population_years_df.transpose()

    #Replace empty values with 0
	population_countries_df = population_countries_df.fillna(0)
	population_years_df = population_years_df.fillna(0)
	
	#Set the column names for the years dataframe
	population_countries_df.columns = population_countries_df.iloc[0]
	population_countries_df = population_countries_df.iloc[1:]
	population_countries_df.index.name = 'Year'
	
	#Set the column names for the years dataframe
	population_years_df = population_years_df.rename(columns={'Country Name': 'Year'})
	population_years_df = population_years_df.set_index('Year')

	return population_years_df, population_countries_df

# Call the function to process the population data
population_years_df, population_countries_df = process_population_data('population.csv')
print(population_years_df)
print(population_countries_df)

# Exploring the Statistical Properties
population_years_df.describe
population_countries_df.describe

import numpy as np
year_array = population_years_df.to_numpy()

# Use numpy functions to find out mean, median, std
np.mean(year_array)
np.median(year_array)
np.std(year_array)

# Getting the top 10 highest countires data population
population_years_df.nlargest(10, '2020')

# Getting the top 10 lowset countires data population
population_years_df.nsmallest(10, '2020')

population_years_df.info()
population_countries_df.info()


"""
Correlations 

Looking at the data above, for the statistics in terms of population and years of the data we are taking 
mean, std devation, and median of the values as we can see median and standard devaiation
values are with in the range and the finally the data is some how we can predictable.

"""


# PLOTTING THE VISUALIZATIONS
# BAR PLOT

import matplotlib.pyplot as plt

# Load the data from the CSV file
population_df = pd.read_csv("population.csv", skiprows=4)

countries = ['Arab World', 'Bangladesh', 'Germany', 'Japan', 'Pakistan', 'Brazil', 'North America']

# Select the relevant columns and rows
population_df_countries = population_df.loc[population_df['Country Name'].isin(countries), ['Country Name', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']]

# Set the index to be the country names
population_df_countries.set_index('Country Name', inplace=True)

# Set the figure size and create a new subplot
plt.figure(figsize=(12, 6))
ax = plt.subplot()

# Set the years and the number of bars per group
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
n_bars = len(years)

# Set the bar width and the offset between the groups
bar_width = 0.8 / n_bars
offset = bar_width / 2

# Set the colors for each year
colors = ['#2b83ba', '#abdda4', '#ffffbf', '#fdae61', '#d7191c', '#2b83ba', '#abdda4', '#ffffbf', '#fdae61', '#d7191c']

# Set the x ticks to be the country names
x_ticks = population_df_countries.index

# Plot the bars for each year
for i, year in enumerate(years):
    ax.bar([j + offset + bar_width*i for j in range(len(x_ticks))], population_df_countries[year], width=bar_width, label=year, color=colors[i])

# Set the axis labels and title
ax.set_xlabel('Country Names')
ax.set_ylabel('Data population in terms of crores')
ax.set_title('Population Statistics by Country and Year')

# Set the x ticks and labels
ax.set_xticks([j + 0.4 for j in range(len(x_ticks))])
ax.set_xticklabels(x_ticks, rotation=60)

# Add a legend
ax.legend()

# Show the plot
plt.show()


# PLOTTING THE VISUALIZATIONS
# LINE PLOT

# Read the male data
male_df = pd.read_csv('male.csv', skiprows=4)

# Create a new DataFrame for the selected countries
male_selected_countries_df = male_df[male_df['Country Name'].isin(countries)].set_index('Country Name').loc[:, '2012':'2020']

# Transpose the DataFrame
male_selected_countries_df = male_selected_countries_df.transpose()
#print(selected_countries_df)

# Plot the data
male_selected_countries_df.plot(figsize=(10, 6))
plt.xlabel('Years')
plt.ylabel('Male Population in Millions')
plt.title('Male Population in Different Countries and Years')
plt.legend(title='Country Names', bbox_to_anchor =(1, 1), ncol = 1)
plt.show()

# Read the female data
female_df = pd.read_csv('female.csv', skiprows=4)

# Create a new DataFrame for the selected countries
female_selected_countries_df = female_df[female_df['Country Name'].isin(countries)].set_index('Country Name').loc[:, '2012':'2020']

# Transpose the DataFrame
female_selected_countries_df = female_selected_countries_df.T

# Plot the data
female_selected_countries_df.plot(figsize=(10, 6))
plt.xlabel('Years')
plt.ylabel('Female Population in Millions')
plt.title('Female Population in Different Countries and Years')
plt.legend(title='Country Names', bbox_to_anchor=(1, 1), ncol = 1)
plt.show()
