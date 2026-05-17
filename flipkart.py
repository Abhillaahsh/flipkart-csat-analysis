#Importing Important Libraries. 
import pandas as pd 
import numpy as np 
import sys
import matplotlib.pyplot as plt 
from matplotlib import colormaps 
import seaborn as sns
from IPython.display import display, HTML 
#Importing Warning Library in order to avoid unnecessary warning.
import warnings
warnings.filterwarnings("ignore") 
#Loading the Data Set
DataSet  = "Customer_support_data.csv"
dataset = r"/Users/abhillaahsh/Downloads/Flipkart project/Customer_support_data.csv"
loaded_csv = pd.read_csv(DataSet)
print(loaded_csv)
# sys.exit()

# display(HTML("<b>bataframe shape:</b>"))
print(f"shape:{loaded_csv.shape}\n")

# display(HTML("<b>dataframe information:</b>"))
print(f"{loaded_csv.info()}\n") 

# Null Values count
NullValues = loaded_csv.isnull().sum()
# NuLl Value Percentage Present
NV_Percentage = round(loaded_csv.isnull() .sum()/len(loaded_csv)*100,0)
print ("\n")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# chart-1 shows null values in %.
sns.barplot(x=NV_Percentage.index, y=NV_Percentage.values, edgecolor="black", linewidth=1, palette='PuBuGn',ax=axes[0] )
axes[0].set_xlabel("Columns", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Missing Values (%)", fontsize=12, fontweight='bold') 
axes[0].set_xticklabels(NV_Percentage.index, rotation=90)
axes[0].set_title("Percentage of Missing Values in Each Column",fontweight='bold'
, pad =20)
# chart-2 Null Values Distribution Across Columns.
sns.barplot(x=NullValues.index, y=NullValues.values, edgecolor="black", linewidth=1, palette='magma',ax=axes [1] )
axes [1].set_xlabel("Columns", fontsize=12, fontweight='bold')
axes [1].set_ylabel("Missing Values Count", fontsize=12, fontweight='bold') 
axes[1].set_xticklabels(NV_Percentage.index, rotation=90)
axes [1].set_title("Null Values Distribution Across Columns",fontweight='bold', pad =20)
plt. tight_layout()
plt. show()
print ("\n")

# 1. missing value heatmap
print("\n")
plt.figure(figsize=(10, 6))
sns.heatmap(loaded_csv.isnull(), cmap='viridis', cbar=True)
plt.title("missing value heatmap")
plt.show()
print("\n")

# Dato CLeaning Steps
# 1. Removing all the Duplicates.
loaded_csv_cleaned = loaded_csv.drop_duplicates()
# 2. Replacing Null values with Default values.
loaded_csv_cleaned.fillna({ "Customer Remarks": "No Feedback Provided",
                             "Customer _City": "Not Mentioned",
                             "Product_category" : "Not Available",
                             "Item_price" : loaded_csv_cleaned["Item_price"].median(),
                             "Order_id" : "Not Available"
      },inplace = True)

# 3. Deleting the Unnecessary Columns
loaded_csv_cleaned = loaded_csv_cleaned.drop(columns = ["order_date_time", "connected_handling_time"])
# 4. Data Standarization
# Converting the columns into Date data type
DateTime = ['Issue_reported at', 'issue_responded', 'Survey_response_Date']
for col in DateTime:
    loaded_csv_cleaned[col] = pd.to_datetime(loaded_csv_cleaned[col],dayfirst= True, errors="coerce")

# changing columns name
loaded_csv_cleaned = loaded_csv_cleaned.rename(columns = {"channel_name": "Channel Name",
                "category": "Category",
                "Order_id": "Order id",
                "Issue_reported at" : "Issue Reported At",
                "issue_responded": "Issue Responded",
                "Survey_response_Date": "Survey Response Date",
                "Customer_City" : "Customer City",
                "Product_category" : "Product Category",
                "Item_price":"Item Price",
                "Agent_name" : "Agent Name"
               })
# setting column(Unique id) as index values.
loaded_csv_cleaned = loaded_csv_cleaned.set_index("Unique id")
loaded_csv_cleaned ["Customer Remarks"] = loaded_csv_cleaned["Customer Remarks"].str.rstrip()


# Important Information related to Dataframe.
# Dataset Columns
# display(HTML("<b>Columns of the Data set:</b>"))
print(f"{loaded_csv_cleaned.columns}\n\n")
      
# Dataset Describtion
# display(HTML("‹b>Important information about the Dataset:</b>"))
print(loaded_csv_cleaned.describe()) 
# sys.exit()

# Check Unique Values for each variable.
unique_values = loaded_csv_cleaned.nunique()
# display(HTML("<b>Unique Values:</b>"))
print(f"{unique_values}\n\n")


# Top 5 Rowa of the Data set 
print(loaded_csv_cleaned.head())


# Univariate Analysi.
# Chart No.1 - Pie Char
ChannelName = loaded_csv_cleaned ["Channel Name"].value_counts().index
Channelcount = loaded_csv_cleaned ["Channel Name"].value_counts().values
explode = (0,0.1,0)
print ("\n")
fig,ax = plt.subplots(figsize=(12, 4))
ax.set_position([0.2, 0.2, 0.6, 0.6])
ax.pie(Channelcount, labels=ChannelName, autopct='%1.1f%%' ,
     startangle=90, explode=explode, shadow = True)
ax.axis("equal")
plt.title("Univariate Analysis\n Channel-Wise Breakdown of Resolved Queries", fontweight='bold', pad= 20)
plt.tight_layout()
plt.show()
print("\n")



# Univariate Analysis
Category = loaded_csv_cleaned["Category"].value_counts().index
CategoryValues = loaded_csv_cleaned[ "Category"].value_counts().values

# Chart No.2 - Bar Chart
print("\n" )
fig,ax = plt.subplots (figsize=(12, 5))
sns.barplot(x = Category, y=CategoryValues,edgecolor="black", linewidth=1, palette = "icefire")
ax.set_xlabel("Category Type", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)
ax.set_xticklabels(Category, rotation=90)
ax.set_title("Frequency Distribution of Categories",fontweight='bold', pad =20)
plt. show()
print("\n")


# Univariate Analysis
SubCategory = loaded_csv_cleaned["Sub-category"].value_counts().index
SubCategoryValues = loaded_csv_cleaned["Sub-category"]. value_counts().values
# Chart No.3 - Bar Chart
print("\n")
fig,ax = plt.subplots(figsize=(12, 5))
sns.barplot(x = SubCategory[:10], y=SubCategoryValues[:10],edgecolor="black", linewidth=1, palette = "Paired")
ax.set_xlabel("Columns", fontsize=12)
ax.set_ylabel("Count Values", fontsize=12)
ax.set_xticklabels(SubCategory, rotation=90)
ax.set_title("Different types of sub-Category Count Frequency" ,fontweight='bold', pad =20)
plt.show()
print("\n")   


# Chart No.4 - Bar Chart
print ("\n")
fig,ax = plt.subplots(figsize=(12, 5))
sns.histplot(x = "CSAT Score", data = loaded_csv_cleaned ,bins = 15,binwidth=0.2, kde = True, edgecolor="black",linewidth=1, color='lightgreen')
ax.set_xlabel("CSAT Score",fontsize=12)
ax.set_ylabel ("Frequency", fontsize=12)
ax.set_title("Customer Satisfaction Score Distribution",fontweight='bold', pad =20) 
plt.show()
print("\n")


# Bivariate & Multivariate Analysis
print("\n")
fig, axes = plt.subplots(figsize=(12,4))
sns.scatterplot(x="CSAT Score", y="Item Price", hue="Channel Name", data=loaded_csv_cleaned, palette='tab10')
axes.set_xlabel("Columns", fontsize=12)
axes.set_ylabel("Count Values", fontsize=12)
axes.set_title("Distribution : CSAT Score VS Item Price" ,fontweight='bold', pad =20) 
plt.legend (loc="upper right")
plt.show()
print("\n")



CategoryData= loaded_csv_cleaned[loaded_csv_cleaned["Category"].isin(['Returns', 'Refund Related', 'Cancellation', 'Feedback', 'Order Related'])]
print ("\n")
sns.set_style("darkgrid")
sns.catplot(x='Category',y='CSAT Score', kind='violin',hue='Channel Name' ,dodge =True, data=CategoryData,
             height=4, aspect=2.5, palette = "colorblind")
plt.xticks(rotation=45)
plt.title("Distribution :Category VS CSAT Score", fontweight='bold', pad =20)
plt.show()
print ("\n")


# Bivariate & Multivariate Analvsis
# CSAT Score vs. Issue Category
print ("\n")
plt.figure(figsize=(13, 4))
sns.boxplot(x='Sub-category', y='CSAT Score', data=loaded_csv_cleaned, palette='muted')
plt.xticks(rotation=90)
plt.title("CSAT Score by Issue Sub-category" ,fontweight='bold' ,pad =20)
plt.show()
print("\n")


# calculating Response time in Minutes.
RP_time= loaded_csv_cleaned[ 'Issue Responded'] - loaded_csv_cleaned[ 'Issue Reported At']
RP_time = RP_time.dt.total_seconds() / 60

print ("\n")
fig, axes = plt.subplots(figsize=(13,4))
sns.lineplot(x='CSAT Score', y=RP_time, data=loaded_csv_cleaned, hue='Channel Name', palette ="CMRmap", ax=axes)
axes.set_xlabel("CSAT Score")
axes.set_ylabel ("Response Time (minutes)")
axes.set_title("CSAT Score vs Response Time")
plt.show()
print("\n")


print ("\n" )
g = sns.JointGrid(x=loaded_csv_cleaned["CSAT Score"].value_counts().index, y =loaded_csv_cleaned ["CSAT Score"].value_counts().values)
g.plot(sns.kdeplot, sns.barplot, edgecolor = "black", fill = True, palette = "crest_r", color = "grey")
g.set_axis_labels (xlabel = "CSAT Score", ylabel = "Frequency")
plt.show()
print("\n")