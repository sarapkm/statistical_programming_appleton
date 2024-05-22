#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'Datasetappleton.csv'
df = pd.read_csv(file)
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Days'] = (df['Date'] - df['Date'].min()).dt.days

#Histogram for surface water levels
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
axs[0].hist(df['Surface water levels (m)'], bins=20, color='blue', alpha=0.7, edgecolor='black')
axs[0].set_title('Histogram of Surface Water Levels')
axs[0].set_xlabel('Surface Water Level (m)')
axs[0].set_ylabel('Frequency')
axs[0].grid(False)

#Average of Surface water levels
average1 = df['Surface water levels (m)'].mean()
print("Average of daily surface water levels:", average1)

# Plot histogram for total precipitation
axs[1].hist(df['Total Precipitation (mm)'], bins=20, color='green', alpha=0.7, edgecolor='black')
axs[1].set_title('Histogram of Total Precipitation')
axs[1].set_xlabel('Total Precipitation (mm)')
axs[1].set_ylabel('Frequency')
axs[1].grid(False)
plt.tight_layout()

#Average of total precipitation
average2 = df['Total Precipitation (mm)'].mean()
print("Average of daily precipitation:", average2)

#Scatterplot comparing both total precipitation with surface water levels
plt.figure(figsize=(8, 6))
plt.scatter(df['Total Precipitation (mm)'], df['Surface water levels (m)'], color='red', alpha=0.5)
z = np.polyfit(df['Total Precipitation (mm)'], df['Surface water levels (m)'], 1)
p = np.poly1d(z)
plt.plot(df['Total Precipitation (mm)'], p(df['Total Precipitation (mm)']), color='blue', label='Trendline');
plt.title('Daily Surface Water Levels vs Total Precipitation')
plt.xlabel('Total Precipitation (mm)')
plt.ylabel('Surface Water Level (m)')
plt.grid(False)
plt.show()

#Scatterplot of daily surface water levels over the course of 2012
plt.figure(figsize=(8, 6))
plt.scatter(df['Days'], df['Surface water levels (m)'], color='blue', alpha=0.5)
z = np.polyfit(df['Days'], df['Surface water levels (m)'], 1)
p = np.poly1d(z)
plt.plot(df['Days'], p(df['Days']), color='red', label='Trendline');
plt.title('Daily Surface Water Levels in 2012')
plt.xlabel('Date (2012)')
plt.ylabel('Surface Water Level (m)')
plt.grid(False)
plt.show()

#Scatterplot of daily Total Precipitation over the course of 2012
plt.figure(figsize=(8, 6))
plt.scatter(df['Days'], df['Total Precipitation (mm)'], color='red', alpha=0.5)
z = np.polyfit(df['Days'], df['Total Precipitation (mm)'], 1)
p = np.poly1d(z)
plt.plot(df['Days'], p(df['Days']), color='blue', label='Trendline');
plt.title('Daily Precipitation in 2012')
plt.xlabel('Date (2012)')
plt.ylabel('Total Precipitation (mm)')
plt.grid(False)
plt.show()

