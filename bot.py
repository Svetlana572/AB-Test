#!/usr/bin/env python
# coding: utf-8

# In[4]:


import telegram
import io
import pandas as pd
import pandahouse as ph
import os      


def test_report(chat=None):
    chat_id = 1978263659
    bot = telegram.Bot(token='5272907074:AAE1jhdOONh6VC2TMj1q6wGfuisw9ON0UJ4')
    
    connection = {'host': 'http://clickhouse.beslan.pro:8080',
                      'database':'simulator_20220120',
                      'user':'student', 
                      'password':'dpo_python_2020'
                     }

    query = "select * from {db}.feed_actions where toDate(time) = yesterday() "
    df = ph.read_clickhouse(query, connection=connection)
    
    
    dau = df.user_id.nunique()
    msg = 'DAU = {} пользователей'.format(dau)
    bot.sendMessage(chat_id=chat_id, text=msg)


try:
    test_report()
except Exception as e:
    print(e)

