#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[7]:


df = pd.read_excel('cleaned__smartphone_data.xlsx')


# In[8]:


df.head()


# In[9]:


df.describe()


# In[10]:


df.info()


# In[11]:


# plot a graph of top 10 brands
df['brand_name'].value_counts().head(10).plot(kind='bar')
plt.savefig("brands.png", dpi=300, bbox_inches="tight")


# In[12]:


# pie chart
df['brand_name'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(8,8))


# In[13]:


df['brand_name'].isnull().sum()


# In[14]:


# model
df['model'].nunique()


# In[15]:


# price
df['price'].describe()


# In[16]:


sns.displot(kind='hist',data=df,x='price',kde=True)
plt.savefig("price_kde.png", dpi=300, bbox_inches="tight")


# In[17]:


df['price'].skew()


# In[18]:


sns.boxplot(df['price'])
plt.savefig("price_boxplot.png", dpi=300, bbox_inches="tight")


# ### Conclusion-price column
# - Price is column is heavily skewed
# - Not many outliers are present
# - The minimum price is  3500.000000 and the maximum is 216999.000000

# In[19]:


df['rating'].describe()


# In[20]:


df['rating'].skew()


# In[21]:


sns.boxplot(df['rating'])
plt.savefig("rating_boxplot.png", dpi=300, bbox_inches="tight")


# In[22]:


df['rating'].isna().sum()


# In[23]:


#has5g
df['has_5g'].value_counts().plot(kind='pie',autopct='%0.1f%%')
plt.savefig("has_5g_pie.png", dpi=300, bbox_inches="tight")


# In[24]:


#hasnfc
df['has_nfc'].value_counts().plot(kind='pie',autopct='%0.1f%%')
plt.savefig("has_nfc.png", dpi=300, bbox_inches="tight")


# In[25]:


#has_ir_blaster
df['has_ir_blaster'].value_counts().plot(kind='pie',autopct='%0.1f%%')
plt.savefig("has_ir_blaster_pie.png", dpi=300, bbox_inches="tight")


# In[26]:


df[df['has_ir_blaster']==True]['brand_name'].value_counts()


# In[27]:


df['processor_brand'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(6,6))


# In[28]:


df['num_cores'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(6,6))


# In[29]:


df['fast_charging_available'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(6,6))
plt.savefig("fast_charging_available_pie.png", dpi=300, bbox_inches="tight")


# In[30]:


df['ram_capacity'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(6,6))
plt.savefig("ram_capacity_pie.png", dpi=300, bbox_inches="tight")


# In[31]:


df['internal_memory'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(6,6))
plt.savefig("internal_memory_pie.png", dpi=300, bbox_inches="tight")


# In[32]:


df['refresh_rate'].value_counts().plot(kind='pie',autopct='%0.1f%%',figsize=(6,6))
plt.savefig("refresh_rate_pie.png", dpi=300, bbox_inches="tight")


# In[33]:


df['refresh_rate'].value_counts()


# In[34]:


df['num_front_camera'] = (df['num_front_camera'].replace("Missing", np.nan).astype("Int64")                 )


# In[35]:


(df['num_rear_cameras']+df['num_front_camera']).value_counts().plot(kind='pie',autopct='%0.1f%%')
plt.savefig("num_rear_cameras_pie.png", dpi=300, bbox_inches="tight")


# In[36]:


df['os'].value_counts().plot(kind='pie',autopct='%0.1f%%')
plt.savefig("os_pie.png", dpi=300, bbox_inches="tight")


# In[37]:


df['extended_memory'].value_counts().plot(kind='pie',autopct='%0.1f%%')
plt.savefig("extended_memory_pie.png", dpi=300, bbox_inches="tight")


# In[38]:


df['screen_size'].plot(kind='box')
plt.savefig("screen_size_pie.png", dpi=300, bbox_inches="tight")


# In[39]:


# Dictionary for better readability
pretty_labels = {
    "brand_name": "Brand",
    "model": "Model",
    "price": "Price (INR)",
    "rating": "Customer Rating",
    "has_5g": "5G Support",
    "has_nfc": "NFC Support",
    "has_ir_blaster": "IR Blaster",
    "processor_brand": "Processor Brand",
    "num_cores": "CPU Cores",
    "processor_speed": "Processor Speed (GHz)",
    "ram_capacity": "RAM (GB)",
    "internal_memory": "Internal Storage (GB)",
    "battery_capacity": "Battery (mAh)",
    "fast_charging_available": "Fast Charging Available",
    "fast_charging": "Fast Charging Power (W)",
    "screen_size": "Screen Size (inches)",
    "resolution": "Resolution",
    "refresh_rate": "Refresh Rate (Hz)",
    "num_rear_cameras": "Rear Cameras (count)",
    "num_front_camera": "Front Cameras (count)",
    "primary_camera_rear": "Primary Rear Camera (MP)",
    "primary_camera_front": "Primary Front Camera (MP)",
    "memory_card_supported": "Memory Card Support",
    "extended_memory": "Extended Memory (GB)",
    "os": "Operating System"
}


def plot_graphs(column_name):
    label = pretty_labels.get(column_name, column_name)  # fallback to original
    # Histogram with FacetGrid
    g = sns.displot(df, x=column_name, kde=True, height=4, aspect=1.3)
    g.set_axis_labels(label, "Count")
    g.fig.suptitle(f"Distribution of {label}", fontsize=14)
    plt.tight_layout()

    # Boxplot with brand as hue 
    g2 = sns.catplot(data=df, x="brand_name", y=column_name, kind="box", height=5, aspect=1.5)
    g2.set_axis_labels("Brand", label)
    g2.fig.suptitle(f"Boxplot of {label} by Brand", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"plot_{label}.png", dpi=300, bbox_inches="tight")

# Numeric columns to plot
num_columns = df.iloc[:, [3,4,6,9,13,14,16]].select_dtypes(include=['float64','int64']).columns

for col in num_columns:
    plot_graphs(col)


# In[40]:


df.head()


# In[41]:


plt.figure(figsize=(20,10))
sns.barplot(data=df,x='brand_name',y='price')
plt.xticks(rotation='vertical')
plt.savefig("brand_name_barplot.png", dpi=300, bbox_inches="tight")


# In[42]:


x = df.groupby('brand_name').count()['model'] 


# In[43]:


temp_df = df[df['brand_name'].isin(x[x > 10].index)]


# In[44]:


plt.figure(figsize=(15,8))
sns.barplot(data=temp_df,x='brand_name',y='price')
plt.xticks(rotation='vertical')


# In[45]:


df.head()


# In[46]:


sns.scatterplot(data=df,x='rating',y='price')
plt.savefig("rating_scatter.png", dpi=300, bbox_inches="tight")


# In[47]:


sns.barplot(data=temp_df,x='has_5g',y='price',estimator=np.median)
plt.savefig("has_5g_plot.png", dpi=300, bbox_inches="tight")


# In[48]:


sns.pointplot(data=temp_df,x='has_nfc',y='price',estimator=np.median)
plt.savefig("has_nfc_point.png", dpi=300, bbox_inches="tight")


# In[49]:


sns.barplot(data=temp_df,x='has_ir_blaster',y='price',estimator=np.median)
plt.savefig("has_ir_blaster_bar.png", dpi=300, bbox_inches="tight")


# In[50]:


sns.barplot(data=temp_df,x='processor_brand',y='price',estimator=np.median)
plt.xticks(rotation='vertical')
plt.savefig("processor_brand_bar.png", dpi=300, bbox_inches="tight")


# In[51]:


sns.barplot(data=temp_df,x='num_cores',y='price',estimator=np.median)
plt.xticks(rotation='vertical')
plt.savefig("num_cores_bar.png", dpi=300, bbox_inches="tight")


# In[52]:


pd.crosstab(df['num_cores'],df['os'])


# In[53]:


sns.scatterplot(data=df,x='processor_speed',y='price')
plt.savefig("processor_speed_scatter.png", dpi=300, bbox_inches="tight")


# In[54]:


sns.scatterplot(data=df,x='screen_size',y='price')
plt.savefig("screen_size_scatter.png", dpi=300, bbox_inches="tight")


# In[55]:


corr_price = df.select_dtypes(include=['number']).corr()['price'].sort_values(ascending=False)

print(corr_price)


# In[56]:


df.isnull().sum()


# In[57]:


corr_price = df.select_dtypes(include=['number']).corr()['rating'].sort_values(ascending=False)

print(corr_price)


# ### KNN IMPUTER TO FILL MISSING VALUES BY PREDICTING

# In[58]:


df.shape


# In[59]:


x_df = df.select_dtypes(include=['int64','float64']).drop(columns='price')


# In[60]:


from sklearn.impute import KNNImputer


# In[61]:


imputer = KNNImputer(n_neighbors=5)


# In[62]:


x_df_values = imputer.fit_transform(x_df)
x_df = pd.DataFrame(x_df_values,columns=x_df.columns)
x_df['price'] = df['price']


# In[63]:


x_df.head()


# In[64]:


a = x_df.corr()['price'].reset_index()


# In[65]:


b = df.select_dtypes(include=['number']).corr()['price'].reset_index()


# In[66]:


b.merge(a,on='index')


# In[67]:


df_corr = df.drop(columns=['model_name', 'phone_name'], errors='ignore')

df_corr = pd.get_dummies(df_corr, columns=['brand_name', 'processor_brand', 'os'], drop_first=True)

correlation_with_price = df_corr.corr(numeric_only=True)['price'].sort_values(ascending=False)

print(correlation_with_price)


# In[68]:


x_df.shape


# In[69]:


sns.histplot(df['price'], kde=True)
plt.show()


# In[ ]:





# In[ ]:




