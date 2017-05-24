import os
import calendar
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Question: What are the most common reasons Armenians visit local pubs?

# Following "Awesome" structure = OSEMN (Obtain, Scrub, Explore, Model, iNterpret)

# Step 1 of OSEMN => Obtain Data
THINK_DIR = "/Users/twaddy/NOTES/thinkful/DataSciBootCampPrep/"
PRESENT_DIR = os.path.join(THINK_DIR, 'assignment_presentation','armenian_pubs')

armenian_pubs_fp = os.path.join(THINK_DIR,'assignment_data/', 'armenian_pubs.csv') # fp = File Path
df = pd.read_csv(armenian_pubs_fp)

# Step 2 of OSEMN => Scrub Data ... strip whitespace, date strings to datetime
df = df.rename(columns=lambda x: x.strip())
df['Timestamp'] = pd.to_datetime(df.Timestamp).dt.date  # Rounds datetime to date, strips time

# Step 3 of OSEMN => Explore Data
print("\nWe have {0} observations in {1} columns".format(df.shape[0], df.shape[1]))
#orig_cols = ['Timestamp' 'Age' ''Gender'' 'Income' 'Occupation' 'Fav_Pub' 'WTS' 'Freq' 'Prim_Imp' 'Sec_Imp' 'Stratum' 'Lifestyle' 'Occasions']

df_see = df.copy(deep=True)
# df_see['day'] = df.Timestamp.apply(lambda x: calendar.day_name[x.weekday()])
# df_see.day.value_counts().plot(kind='bar', title="Day of the Week", width=0.5)
# plot_of_days_bar_fp   = os.path.join(PRESENT_DIR, 'day_of_week_bar_chart.png')
# plot_of_days_bar_link = os.path.join(PRESENT_DIR, 'presentation.1.png')
# plt.tight_layout()
# plt.savefig(plot_of_days_bar_fp)
# os.system("open -a preview {0}".format(plot_of_days_bar_fp))
# os.system("ln -s {0} {1}".format(plot_of_days_bar_fp, plot_of_days_bar_link))

# df_see.Timestamp.value_counts().plot(kind='bar', title="Date", width=0.5)
# plt.tight_layout()
# plot_of_days_bar_fp   = os.path.join(PRESENT_DIR, 'date_bar_chart.png')
# plot_of_days_bar_link = os.path.join(PRESENT_DIR, 'presentation.2.png')
# plt.tight_layout()
# plt.savefig(plot_of_days_bar_fp)
# os.system("open -a preview {0}".format(plot_of_days_bar_fp))
# os.system("ln -s {0} {1}".format(plot_of_days_bar_fp, plot_of_days_bar_link))


# df = df.sort_values('Timestamp', ascending=True)
# df.plot(kind='scatter', x=df.columns[x], y=df.columns[y])  # The least error prone syntax
# xticks = pd.date_range(start=start_day, end=end_day, freq='W-Tue')


# df_see.Prim_Imp.value_counts().plot(kind='bar', title="First Impressions", width=0.5)
# plt.tight_layout()
# plot_of_days_bar_fp   = os.path.join(PRESENT_DIR, 'first_impressions_bar_chart.png')
# plot_of_days_bar_link = os.path.join(PRESENT_DIR, 'presentation.3.png')
# plt.tight_layout()
# plt.savefig(plot_of_days_bar_fp)
# os.system("open -a preview {0}".format(plot_of_days_bar_fp))
# os.system("ln -s {0} {1}".format(plot_of_days_bar_fp, plot_of_days_bar_link))


df_see.Prim_Imp.value_counts().plot(kind='bar', title="Secondary Impressions", width=0.5)
plt.tight_layout()
plot_of_days_bar_fp   = os.path.join(PRESENT_DIR, 'second_impressions_bar_chart.png')
plot_of_days_bar_link = os.path.join(PRESENT_DIR, 'presentation.4.png')
plt.tight_layout()
plt.savefig(plot_of_days_bar_fp)
os.system("open -a preview {0}".format(plot_of_days_bar_fp))
os.system("ln -s {0} {1}".format(plot_of_days_bar_fp, plot_of_days_bar_link))


