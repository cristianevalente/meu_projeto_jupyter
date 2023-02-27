#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.read_csv('dados/aluguel.csv')


# In[3]:


pd.read_csv('dados/aluguel.csv', sep=';')


# In[4]:


dados=pd.read_csv('dados/aluguel.csv', sep=";")


# In[5]:


type(dados)


# In[6]:


dados.info()


# #Relatório de Análise I

# In[7]:


##Importando a Base de Dados


# In[8]:


dados.head(10)


# In[9]:


dados.head()


# In[10]:


##Informações Gerais sobre a Base de Dados


# In[11]:


dados.dtypes


# In[12]:


pd.DataFrame(dados.dtypes)


# In[13]:


pd.DataFrame(dados.dtypes, columns=['Tipos de Dados'])


# In[14]:


tipos_de_dados=pd.DataFrame(dados.dtypes, columns=['Tipos de Dados'])


# In[15]:


tipos_de_dados.columns.name="Variáveis"
tipos_de_dados


# In[16]:


dados.shape


# In[17]:


dados.shape[0]


# In[18]:


dados.shape[1]


# In[19]:


print('A base de dados apresenta {} registros (imóveis) e {} variáveis.'.format(dados.shape[0], dados.shape[1]))


# In[20]:


import pandas as pd
data=[['Fulano', 12, 7.0, True],
['Sicrano', 15, 3.5, False],
['Beltrano', 18, 9.3, True]]
dados=pd.DataFrame(data,columns=['Aluno', 'Idade', 'Nota','Aprovado'])
dados


# In[21]:


tipos_de_dados = pd.DataFrame(dados.dtypes,
    columns = ['Tipos de Dados'])
tipos_de_dados.columns.name = 'Variáveis'
tipos_de_dados


# In[22]:


get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# In[27]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.federalreserve.gov/releases/h3/current/default.htm'
response=requests.get(url)
html=response.content
soup=BeautifulSoup(html,'html.parser')
table=soup.findAll('table')
html_file=f'<html><body>{table}</body></html>'
df=pd.read_html(html_file)
df[0]

import requests
from bs4 import BeautifulSoup
import pandas as pd
df[0]



#Como a função read_html retorna uma lista de Dataframe, basta acessar as tabelas pelos índices da lista.
#Como temos três tabelas na página usamos os índices 0, 1 ou 2 para acessar os DataFrames que buscamos


# In[ ]:




