import pandas as pd
import numpy as np

def cleanEnergyData(energy):
    # remove garbage columns
    energy.drop(['Unnamed: 0', 'Unnamed: 1'], axis = 1, inplace = True)
    # replace missing data with NaN
    energy = energy.replace('...', np.NaN)
    # update columns
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    # fix country names
    energy['Country'] = energy['Country'].replace('Republic of Korea', 'South Korea')
    energy['Country'] = energy['Country'].replace('United States of America', 'United States')
    energy['Country'] = energy['Country'].replace('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom')
    energy['Country'] = energy['Country'].replace('China, Hong Kong Special Administrative Region', 'Hong Kong')
    # remove numerical values
    energy['Country'] = energy['Country'].replace('\d+', '')
    # remove parentheses
    energy['Country'] = energy['Country'].replace(r"\(.*\)","")

    return energy

def cleanGDPData(GDP):
    GDP['Country Name'] = GDP['Country Name'].replace('Korea, Rep.', 'South Korea')
    GDP['Country Name'] = GDP['Country Name'].replace('Iran, Islamic Rep.', 'Iran')
    GDP['Country Name'] = GDP['Country Name'].replace('Hong Kong SAR, China', 'Hong Kong')

    return GDP

# Load the file
def function_one():
    # import energy data (remove header/footer)
    energy = pd.read_excel('Energy Indicators.xls', skiprows=17, skipfooter=38)
    energy = cleanEnergyData(energy)

    # import world bank data
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP = cleanGDPData(GDP)

    # import Sciamgo rank data
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    # merge data
    GDPValidYears = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    GDPValidYears.set_index('Country Name', inplace=True)

    # ScimEnValidRanks = ScimEn.where(ScimEn[''])

    return energy.head()

print(function_one())