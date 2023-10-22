#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
from pandas import DataFrame


# In[2]:


dio_df = pd.read_csv("dataset.csv")


# In[3]:


con = sqlite3.connect('dio_df.db')
cursor = con.cursor()


# In[4]:


dio_df.to_sql('datasetdio', con, if_exists='replace', index=False)


# In[5]:


query1 = 'SELECT * FROM datasetdio'
cursor.execute(query1)


# In[6]:


sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(sql_query)
query1 = 'SELECT * FROM datasetdio'
cursor.execute(query1)


# In[7]:


nome_colunas = [description[0] for description in cursor.description]
print(nome_colunas)


# In[8]:


dados = cursor.fetchall()


# In[9]:


dio_df.isna().sum()


# In[11]:


moda = dio_df['Quantidade'].value_counts().index[0]


# In[12]:


dio_df['Quantidade'].fillna(value = moda, inplace = True)


# In[13]:


dio_df.isna().sum()


# In[16]:


df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'Data_Pedido', 
                                    'ID_Cliente',
                                    'Segmento',
                                    'Pais',
                                    'Regiao',
                                    'ID_Produto',
                                    'Categoria',
                                    'Nome_Produto',
                                    'Valor_Venda',
                                    'Quantidade'])


# In[23]:


dio_df['Ano'] = dio_df['ID_Pedido'].str.split('-').str[1]


# In[46]:


dio_df['Segmento'] = dio_df['Segmento'].str.replace('Home Office', 'Workroom')


# In[48]:


dio_df[ (dio_df.Segmento == 'Workroom')].head()


# In[63]:


query3 = 'SELECT Nome_Produto, AVG(Quantidade) FROM datasetdio GROUP BY Nome_Produto'
cursor.execute(query3)
cursor.fetchall()


# In[55]:


query5 = """SELECT Nome_Produto, AVG(Valor_Venda) 
            FROM datasetdio
            WHERE Valor_Venda > 1990
            GROUP BY Nome_Produto 
            HAVING AVG(Valor_Venda) > 100"""


# In[56]:


cursor.execute(query5)
cursor.fetchall()


# In[ ]:




