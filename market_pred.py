import pandas as pd
import requests
import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import numpy as np
from stocknews import StockNews
from pyChatGPT import ChatGPT

st.markdown("""
    <audio autoplay loop>
        <source src="Scam-1992(PaglaSongs).mp3" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """, unsafe_allow_html=True)
base_url = 'https://financialmodelingprep.com/api'
apikey = 'Wy9h7tdS2JIBadpIs8LaUPA4l5vf3ZoL'


st.header("Paisa Stock Screener")
symbol = st.sidebar.text_input('Ticker: ', value='MSFT')
financial_chart = st.sidebar.selectbox('Visual Charts', options=(
    'Charts','Visual-Charts'
))
if(financial_chart == 'Charts'):
    default_start_date = datetime.date(2024, 2,13)
    start_date = st.sidebar.date_input('Start Date',value=default_start_date)
    end_date = st.sidebar.date_input('End Date')
    financial_chart = yf.download(symbol,start=start_date,end=end_date)
    fig = px.line(financial_chart,x=financial_chart.index,y=financial_chart['Adj Close'],title=symbol)
    st.plotly_chart(fig)
pricing_data,news,price_check = st.tabs(['Pricing Data','News10','Price Checker'])
with pricing_data:
    st.header('Price Movements')
    fin_data = financial_chart
    fin_data['% Change'] = financial_chart['Adj Close'] / financial_chart['Adj Close'].shift(1) - 1
    fin_data.dropna(inplace=True)
    st.write(fin_data)
    annual_return = fin_data['% Change'].mean()*252*100
    st.write('Annual Return = ',annual_return,'%')
    stdev = np.std(fin_data['% Change'])*np.sqrt(252)
    st.write('Standard Deviation = ',stdev*100,'%')
    risk_adj = annual_return/(stdev*100)
    st.write('Risk Adjacency = ',risk_adj)
    if(risk_adj > 1.5):
        st.write('Is Company Considerable = Yes')
    else:
        st.write('Is Company Considerable = No')
with news:
    st.header(f'Top 10 News of {symbol}')
    sn = StockNews(symbol, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment = {news_sentiment}')

with price_check:
    st.header('Price Checker For Reliance, Infosys, TCS')


    # session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..M9yuCwV6qiVfljc2.TedkOGqGZ_PK31T7Pe1nKZg7j40yEwdMq0u-Vv2Q5oTOvJ6LXdhWCleorvSq38FB6OhdfP4XFIZVhXZg-DyB10n7MiR5zbXzWneonYT8bo65NPTqncnj9c67QcUnXYtdGKgkrC4buP8lQseTqTD3qXDa6dficXEjEg-2r34nUr-lVg4_MhHl3V6e8fJGDczVkiye---_QGgQnkGVd7kdSn3qMZ8OyKcYcTSWNdBCMD92y8v9A2IyfV7Cj8-3cw3rT2cbBt1N3OHpMW_eAQDFjzQZNgSFnoolVL27gYsVG-gHaDhzAD7E3OWbgBHrNOcrFwzL2GQnj5cF2ypQHd0UGSKAX-sXiBZAa9NJKROpJI1IdgUxSJiEwcthYTJotN89r7L6LOAw4RzZsn6-q-glJ6YPuA1JkCREoRfxiH_6pM7U5dWIyQQtaQjBwo-5rMfzftWM7UAvk8tf_A5VU3SkncKIM7uPacXFR4Eyr22iJmx5Oty3AeWnny6_QbYGh73QBkr2NbTDWfUP5FSh-MJgiSSlwNg-hSRl48B2QTJ06S6XbrmeN-qj0sB_VuUtg7Gq7BGvhJ4zJ__4S1xNwgytze2GsfGeNSPgd4tA60VCxJHw6hM5JzCYJVMdddf4bizaAj7b1g_T3PrfQw6WZIEh8SxPTd6DQrudi38qj1tg1es46au3vZZemvTY9DXJAPs9DUA7XgoPi_rbLArUj8iqayzoUz76uxu3wbSx-g_nSN-5BHBXNCoep827xhYB1EdN0YuvsriGrTY80ZnLuumDguop5zVMLmu73eeiDb-rNhjaNfjN539A9IJxYcYTgqV0oporK08ljukdMUNRWEDqP8y-R0NDIFtOEjfgk-jMRO_neAvJth2yMpmSakmD-ga0oAcXedZUpihx1DYLM4ZvL2D1bvg7CI-m015V-g__-nKK4HdU5Dt36FA1qf-s4-MvGN5UwcC5WYNsrdWFwUCXO7j_Ffk0O7qv5e76tjHS80GWbRslPDZk6-xlUvKhvCz-tjrh_oine4HkRZpdkQR1LTPHsG8PDvEqR_FoUXS0uIAxBLqzk5CGmxOkOYK8Xh3WfsHplrDXIANdJ_tBC5h6-AM_27LOQmILvir1OnPLcDxHz4L4X40It-lzA-_5JS6sV18KBszE7i68RRxQUukyb5_FwfuQJ_oi__Grl8bIlIdc8wfsH-yBQk969g9ZRpkqb1LEwQA6poZIVhSDyQVuB7Y5a3TRlrPkzLq3Y6b0PNOMR9yG5OQ5HFXBJE7V5FLDGAG4z8zaCDBzEqqKo5By5NXZcy-91zUMALhQ2yu50Ce5KTLsUDl7QJdLEzZcsS9fQRUxmYwmOsLgnQexfAkm3OdOFiwyz2je_BOVLJQuWhyk7Zv9BVa1Y4E0Ue8ZjXwt-4zRmyIc_ix83q_vOwz9wmjWOu2KNa4vKVXVxv1_jvYpm8S5jr_21KgH2BA13j42KwegREQorL02pLZZCOkhhsxsQ16sU4WyjTohLB2mBezbDCD-F-u48kz9ce_1z5Hn1SmMdtNSYreyvjGMQJewY0ZBOj0w26ONHmZq7lq6BasIvHz2YjVhaj1yPJ9XzxDuWn2agXC-dLBNXvccYmFmoeBiveXWaP-hBWU4LYh5Kc6iSv5U-b6Z0mnLDkrMZQMK4SXQVqNNiwDZgUv_zyTr3-KVB-YzB0-txVQfxKh3Iu_OFn9-Vm_IiKyUqU8-S3NtFxtV6vbuARk-AogiWjO9AutbWhqC0Mhne_1mQD-hSOiOZA1vYWh7SW8xbVic40b3DxGkw0VyCaCB5W4fTc19EF14QbSiZcS2te4sPHf2VmtDaIw20PEYRPDe7d37wlBD3vJJvTJfyKZt_ryK-9e4HBg4SleA7P-PlXUySTOB9SZZO8T4ZIQo4t0nFj8ErM5NK-e_R5A3KOPM2E8t2oh1ViRjGcGBiMgfUN2hLlvY1gUEh3gemnd34X4JqptLGRVRyFoVZlz9uapQQHyViMs5QOcEwsjNE92Z3WbhM7VzjE7jrgYNLnP7uLQQNHOPoiELFbFBtrkdXsHQdQb-60Sb-6_ZeeHvPqgBE0lWi1n-eNyARjIdT1mi0T9s0izB680qQ8CuS9UFqDGqgbLJjXuvwwCPbXGwbPEUADXo2jlTZmCArVYZT1C-Z4UXFv1oCwyLPJ3ySHJdauTXJ_FVGp3Ot-G-td29PoPrWiiCGI_F8Kak7xidETKuAAva-RexHofOVlWVCIINxBBvYrEbjRIvnrQ2Z3d1ypdWiI9K0RMsV3v0Osxl313CuH4cSaert6cfo8eCN1ao_3eiw33wXD-151ZwI5IwDG201iF6agMP9v6EXM4APPL16mLoTqDIpd1ZV8qHGlKT8YgvvZAPcK3d3yOEeu29CL4mON6dSRR03UOwd08iaZL5jK2N4Fk2p7RsmNjIOTwJdJ6pQ6MEsSIUloOUDT-BDH26K8CjQv8ZxIXQXPeKAR4o8_tOW6PpvZlQOHXGnSwJqJkAkPlidEs85LE6-8e9dWpCGE0vexpAZdkHV0dHtYi7PXekvtrHaxMCE_gSaJ8Ti2NhO2ic0axWSq41P8x8wb9EaQWiyxzXZ9B8tm4gk9CPzjeqMWtP9qnxKI4sQqd08I2uxhfPZD5zBs0bhhxe9SD3mRPM7Vw3bOBO2ZzROsfEpogX1N5U5X07yfboxMjzsvlY-krVOtOKsCgMmZpLby2x3tVY5BjqMzhBRPXmiSiWmXn0ONjGvOZUPdy2-O_KFbh72qzncdVYUTwGCHoxSuWAg62ZbwjUC2FcJA.K_H9yFnLKWZmZ8O5LOhFMw'
    # gpt = ChatGPT(session_token)
    # buy = gpt.send_message(f'3 Reasons to Buy Stock of {symbol}')
    # sell = gpt.send_message(f'3 Reasons not to Buy Stock of {symbol}')
    # swot = gpt.send_message(f'Swot Analysis of {symbol}')
st.header('Financial Matrix')
financial_data = st.sidebar.selectbox('Financial Data Type', options=(
'income-statement', 'balance-sheet-statement', 'cash-flow-statement', 'income-statement-growth',
'balance-sheet-statement-growth', 'cash-flow-statement-growth', 'key-metrics-ttm', 'enterprise-values', 'rating',
'ratios', 'ratios-ttm', 'quote', 'Historical Price smaller intervals'))
if (financial_data == 'Historical Price smaller intervals'):
    interval = st.sidebar.selectbox('Interval', options=('1min', '5min', '15min', '30min', '1hour', '4hour'))
    financial_data = 'historical-chart/' + interval
transpose = st.sidebar.selectbox('Transpose', options=('Yes', 'No'))

url = f'{base_url}/v3/{financial_data}/{symbol}?period=annual&apikey={apikey}'
response = requests.get(url)
data = response.json()

if transpose == 'Yes':
    df = pd.DataFrame(data).T
else:
    df = pd.DataFrame(data)

st.write(df)
# session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..M9yuCwV6qiVfljc2.TedkOGqGZ_PK31T7Pe1nKZg7j40yEwdMq0u-Vv2Q5oTOvJ6LXdhWCleorvSq38FB6OhdfP4XFIZVhXZg-DyB10n7MiR5zbXzWneonYT8bo65NPTqncnj9c67QcUnXYtdGKgkrC4buP8lQseTqTD3qXDa6dficXEjEg-2r34nUr-lVg4_MhHl3V6e8fJGDczVkiye---_QGgQnkGVd7kdSn3qMZ8OyKcYcTSWNdBCMD92y8v9A2IyfV7Cj8-3cw3rT2cbBt1N3OHpMW_eAQDFjzQZNgSFnoolVL27gYsVG-gHaDhzAD7E3OWbgBHrNOcrFwzL2GQnj5cF2ypQHd0UGSKAX-sXiBZAa9NJKROpJI1IdgUxSJiEwcthYTJotN89r7L6LOAw4RzZsn6-q-glJ6YPuA1JkCREoRfxiH_6pM7U5dWIyQQtaQjBwo-5rMfzftWM7UAvk8tf_A5VU3SkncKIM7uPacXFR4Eyr22iJmx5Oty3AeWnny6_QbYGh73QBkr2NbTDWfUP5FSh-MJgiSSlwNg-hSRl48B2QTJ06S6XbrmeN-qj0sB_VuUtg7Gq7BGvhJ4zJ__4S1xNwgytze2GsfGeNSPgd4tA60VCxJHw6hM5JzCYJVMdddf4bizaAj7b1g_T3PrfQw6WZIEh8SxPTd6DQrudi38qj1tg1es46au3vZZemvTY9DXJAPs9DUA7XgoPi_rbLArUj8iqayzoUz76uxu3wbSx-g_nSN-5BHBXNCoep827xhYB1EdN0YuvsriGrTY80ZnLuumDguop5zVMLmu73eeiDb-rNhjaNfjN539A9IJxYcYTgqV0oporK08ljukdMUNRWEDqP8y-R0NDIFtOEjfgk-jMRO_neAvJth2yMpmSakmD-ga0oAcXedZUpihx1DYLM4ZvL2D1bvg7CI-m015V-g__-nKK4HdU5Dt36FA1qf-s4-MvGN5UwcC5WYNsrdWFwUCXO7j_Ffk0O7qv5e76tjHS80GWbRslPDZk6-xlUvKhvCz-tjrh_oine4HkRZpdkQR1LTPHsG8PDvEqR_FoUXS0uIAxBLqzk5CGmxOkOYK8Xh3WfsHplrDXIANdJ_tBC5h6-AM_27LOQmILvir1OnPLcDxHz4L4X40It-lzA-_5JS6sV18KBszE7i68RRxQUukyb5_FwfuQJ_oi__Grl8bIlIdc8wfsH-yBQk969g9ZRpkqb1LEwQA6poZIVhSDyQVuB7Y5a3TRlrPkzLq3Y6b0PNOMR9yG5OQ5HFXBJE7V5FLDGAG4z8zaCDBzEqqKo5By5NXZcy-91zUMALhQ2yu50Ce5KTLsUDl7QJdLEzZcsS9fQRUxmYwmOsLgnQexfAkm3OdOFiwyz2je_BOVLJQuWhyk7Zv9BVa1Y4E0Ue8ZjXwt-4zRmyIc_ix83q_vOwz9wmjWOu2KNa4vKVXVxv1_jvYpm8S5jr_21KgH2BA13j42KwegREQorL02pLZZCOkhhsxsQ16sU4WyjTohLB2mBezbDCD-F-u48kz9ce_1z5Hn1SmMdtNSYreyvjGMQJewY0ZBOj0w26ONHmZq7lq6BasIvHz2YjVhaj1yPJ9XzxDuWn2agXC-dLBNXvccYmFmoeBiveXWaP-hBWU4LYh5Kc6iSv5U-b6Z0mnLDkrMZQMK4SXQVqNNiwDZgUv_zyTr3-KVB-YzB0-txVQfxKh3Iu_OFn9-Vm_IiKyUqU8-S3NtFxtV6vbuARk-AogiWjO9AutbWhqC0Mhne_1mQD-hSOiOZA1vYWh7SW8xbVic40b3DxGkw0VyCaCB5W4fTc19EF14QbSiZcS2te4sPHf2VmtDaIw20PEYRPDe7d37wlBD3vJJvTJfyKZt_ryK-9e4HBg4SleA7P-PlXUySTOB9SZZO8T4ZIQo4t0nFj8ErM5NK-e_R5A3KOPM2E8t2oh1ViRjGcGBiMgfUN2hLlvY1gUEh3gemnd34X4JqptLGRVRyFoVZlz9uapQQHyViMs5QOcEwsjNE92Z3WbhM7VzjE7jrgYNLnP7uLQQNHOPoiELFbFBtrkdXsHQdQb-60Sb-6_ZeeHvPqgBE0lWi1n-eNyARjIdT1mi0T9s0izB680qQ8CuS9UFqDGqgbLJjXuvwwCPbXGwbPEUADXo2jlTZmCArVYZT1C-Z4UXFv1oCwyLPJ3ySHJdauTXJ_FVGp3Ot-G-td29PoPrWiiCGI_F8Kak7xidETKuAAva-RexHofOVlWVCIINxBBvYrEbjRIvnrQ2Z3d1ypdWiI9K0RMsV3v0Osxl313CuH4cSaert6cfo8eCN1ao_3eiw33wXD-151ZwI5IwDG201iF6agMP9v6EXM4APPL16mLoTqDIpd1ZV8qHGlKT8YgvvZAPcK3d3yOEeu29CL4mON6dSRR03UOwd08iaZL5jK2N4Fk2p7RsmNjIOTwJdJ6pQ6MEsSIUloOUDT-BDH26K8CjQv8ZxIXQXPeKAR4o8_tOW6PpvZlQOHXGnSwJqJkAkPlidEs85LE6-8e9dWpCGE0vexpAZdkHV0dHtYi7PXekvtrHaxMCE_gSaJ8Ti2NhO2ic0axWSq41P8x8wb9EaQWiyxzXZ9B8tm4gk9CPzjeqMWtP9qnxKI4sQqd08I2uxhfPZD5zBs0bhhxe9SD3mRPM7Vw3bOBO2ZzROsfEpogX1N5U5X07yfboxMjzsvlY-krVOtOKsCgMmZpLby2x3tVY5BjqMzhBRPXmiSiWmXn0ONjGvOZUPdy2-O_KFbh72qzncdVYUTwGCHoxSuWAg62ZbwjUC2FcJA.K_H9yFnLKWZmZ8O5LOhFMw'
# gpt = ChatGPT(session_token)
# def process_prompts():
#     buy = gpt.send_message(f'5 Reasons to Buy Stock of {symbol}')
#     sell = gpt.send_message(f'5 Reasons not to Buy Stock of {symbol}')
#     swot = gpt.send_message(f'Swot Analysis of {symbol}')
#     return buy['message'], sell['message'], swot['message']
#
# if st.button('Process Prompts'):
#     buy_reason, sell_reason, swot_analysis = process_prompts()
#
#     with st.expander('Buying Reasons'):
#         st.write(buy_reason)
#
#     with st.expander('Selling Reasons'):
#         st.write(sell_reason)
#
#     with st.expander('SWOT Analysis'):
#         st.write(swot_analysis)


