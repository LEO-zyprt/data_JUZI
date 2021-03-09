from Data_Request_Response import download_juzi
import pandas as pd

df_finance = download_juzi('金融')
df_hardware = download_juzi('智能硬件')
df_software = download_juzi('工具软件')
df_service = download_juzi('企业服务')

df_report = pd.concat([df_finance,df_hardware,df_software,df_service]).sort_values(by='time',ascending=False)
df_report.to_csv(r'C:\Users\ZY\Desktop\weekly_report\weekly.report.csv')