import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

CLIENT_ID = '22CPDQ'
CLIENT_SECRET = '56662aa8bf31823e4137dfbf48a1b5f1'

def main():
    # some copy pasted code to initialize session
    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    # formats the output in year-month-day
    yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
    yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    today = str(datetime.datetime.now().strftime("%Y%m%d"))

    # gets heart activity
    fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')

    
