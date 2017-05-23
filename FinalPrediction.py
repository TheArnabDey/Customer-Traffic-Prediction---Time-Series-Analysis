import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
tracker = pd.read_csv('raka.csv')
s = 1
n = ''
df = pd.read_csv('Contacts_Pre_2017.csv')
for i in range(0,len(df)):
    a = df.iloc[i,0].split('/')
    if a[0] == '1':
        a[0] = '01'
    elif a[0] == '2':
        a[0] = '02'
    elif a[0] == '3':
        a[0] = '03'
    elif a[0] == '4':
        a[0] = '04'
    elif a[0] == '5':
        a[0] = '05'
    elif a[0] == '6':
        a[0] = '06'
    elif a[0] == '7':
        a[0] = '07'
    elif a[0] == '8':
        a[0] = '08'
    elif a[0] == '9':
        a[0] = '09'
    if a[1] == '1':
        a[1] = '01'
    elif a[1] == '2':
        a[1] = '02'
    elif a[1] == '3':
        a[1] = '03'
    elif a[1] == '4':
        a[1] = '04'
    elif a[1] == '5':
        a[1] = '05'
    elif a[1] == '6':
        a[1] = '06'
    elif a[1] == '7':
        a[1] = '07'
    elif a[1] == '8':
        a[1] = '08'
    elif a[1] == '9':
        a[1] = '09'
    df.iloc[i,0] = a[2]+"/"+a[0]+"/"+a[1]
dfi = df.groupby(['START.DATE'])['Contacts'].sum()
dfi = pd.DataFrame(dfi)
dfi.columns = ["Contacts"]
dfi["Index"] = 0
for i in range (0,len(dfi)):
    dfi.iloc[i,1] = i+1
dft = pd.read_csv('Contacts2017.csv')
for i in range(0,len(df)):
    a = df.iloc[i,0].split('/')
    if a[0] == '1':
        a[0] = '01'
    elif a[0] == '2':
        a[0] = '02'
    elif a[0] == '3':
        a[0] = '03'
    elif a[0] == '4':
        a[0] = '04'
    elif a[0] == '5':
        a[0] = '05'
    elif a[0] == '6':
        a[0] = '06'
    elif a[0] == '7':
        a[0] = '07'
    elif a[0] == '8':
        a[0] = '08'
    elif a[0] == '9':
        a[0] = '09'
    if a[1] == '1':
        a[1] = '01'
    elif a[1] == '2':
        a[1] = '02'
    elif a[1] == '3':
        a[1] = '03'
    elif a[1] == '4':
        a[1] = '04'
    elif a[1] == '5':
        a[1] = '05'
    elif a[1] == '6':
        a[1] = '06'
    elif a[1] == '7':
        a[1] = '07'
    elif a[1] == '8':
        a[1] = '08'
    elif a[1] == '9':
        a[1] = '09'
    df.iloc[i,0] = a[2]+"/"+a[0]+"/"+a[1]
dft.iloc[:, 0] = dft.iloc[:, 0].str.replace('/\d\d/\d\d\d\d', '')
dft["IndexSq"] = dft["Index"]**2
dft["Index1"] = dft["Index"]
dft["Jan"] = 0
dft["Feb"] = 0
dft["Mar"] = 0
dft["Apr"] = 0
dft["May"] = 0
dft["Jun"] = 0
dft["Jul"] = 0
dft["Aug"] = 0
dft["Sep"] = 0
dft["Oct"] = 0
dft["Nov"] = 0
dft["IndexSq1"] = dft["Index"]**2
dft["Index2"] = dft["Index"]
dft["Q1"] = 1
dft["Q2"] = 0
dft["Q3"] = 0
dft["IndexSq2"] = dft["Index"]**2
for i in range(0, len(dft)):
    if dft.iloc[i, 0] == '01':
        dft.iloc[i, 7] = 1
    elif dft.iloc[i, 0] == '02':
        dft.iloc[i, 8] = 1
    elif dft.iloc[i, 0] == '03':
        dft.iloc[i, 9] = 1
for m in ('Call - Input', 'Fax - Input','Fax Acknowledgement - Input','Installation Report - Input','Internal Management',
          'Mail - Input','Mail - Recieved','Tweet - Input','Visit','Web - Input'):
    df1 = df.loc[df['CONTACT.TYPE'] == m]
    df1 = df1.groupby(['START.DATE'])['Contacts'].sum()
    df1 = pd.DataFrame(df1)
    df1.columns = ["Contacts"]
    df1["Date"] = df1.index
    df1["Index"] = 0
    for x in range(0, len(df1)):
        for y in range(0, len(dfi)):
            if df1.index[x] == dfi.index[y]:
                df1.iloc[x, 2] = dfi.iloc[y, 1]
    df1["Jan"] = 0
    df1["Feb"] = 0
    df1["Mar"] = 0
    df1["Apr"] = 0
    df1["May"] = 0
    df1["Jun"] = 0
    df1["Jul"] = 0
    df1["Aug"] = 0
    df1["Sep"] = 0
    df1["Oct"] = 0
    df1["Nov"] = 0
    for x in range(0, len(df1)):
        df1.iloc[x, 1] = df1.iloc[x, 1][:7]
    for i in range(0, len(df1)):
        if str(df1.iloc[i, 1]).find('-01') != -1:
            df1.iloc[i, 3] = 1
        if str(df1.iloc[i, 1]).find('-02') != -1:
            df1.iloc[i, 4] = 1
        if str(df1.iloc[i, 1]).find('-03') != -1:
            df1.iloc[i, 5] = 1
        if str(df1.iloc[i, 1]).find('-04') != -1:
            df1.iloc[i, 6] = 1
        if str(df1.iloc[i, 1]).find('-05') != -1:
            df1.iloc[i, 7] = 1
        if str(df1.iloc[i, 1]).find('-06') != -1:
            df1.iloc[i, 8] = 1
        if str(df1.iloc[i, 1]).find('-07') != -1:
            df1.iloc[i, 9] = 1
        if str(df1.iloc[i, 1]).find('-08') != -1:
            df1.iloc[i, 10] = 1
        if str(df1.iloc[i, 1]).find('-09') != -1:
            df1.iloc[i, 11] = 1
        if str(df1.iloc[i, 1]).find('-10') != -1:
            df1.iloc[i, 12] = 1
        if str(df1.iloc[i, 1]).find('-11') != -1:
            df1.iloc[i, 13] = 1
    df1["IndexSq"] = df1["Index"] ** 2
    clf1 = LinearRegression()
    clf1.fit(df1.iloc[:, 2:-1], df1.iloc[:, 0])
    pred = clf1.predict(df1.iloc[:, 2:-1])
    value1 = mean_squared_error(df1.iloc[:, 0], pred)
    clf2 = LinearRegression()
    clf2.fit(df1.iloc[:, 2:], df1.iloc[:, 0])
    pred = clf2.predict(df1.iloc[:, 2:])
    value2 = mean_squared_error(df1.iloc[:, 0], pred)

    df3 = df.loc[df['CONTACT.TYPE'] == m]
    df3 = df3.groupby(['START.DATE'])['Contacts'].sum()
    df3 = pd.DataFrame(df3)
    df3.columns = ["Contacts"]
    df3["Date"] = df3.index
    df3["Index"] = 0
    for x in range(0, len(df3)):
        for y in range(0, len(dfi)):
            if df3.index[x] == dfi.index[y]:
                df3.iloc[x, 2] = dfi.iloc[y, 1]
    for i in range(0, len(df3)):
        df3.iloc[i, 1] = df3.iloc[i, 1][:7]
    df3["Q1"] = 0
    df3["Q2"] = 0
    df3["Q3"] = 0
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-02', '-01')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-03', '-01')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-04', '-02')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-05', '-02')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-06', '-02')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-07', '-03')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-08', '-03')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-09', '-03')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-10', '-04')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-11', '-04')
    df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-12', '-04')
    for i in range(0, len(df3)):
        if str(df3.iloc[i, 1]).find('-01') != -1:
            df3.iloc[i, 3] = 1
        if str(df3.iloc[i, 1]).find('-02') != -1:
            df3.iloc[i, 4] = 1
        if str(df3.iloc[i, 1]).find('-03') != -1:
            df3.iloc[i, 5] = 1
    df3["IndexSq"] = df3["Index"] ** 2
    clf3 = LinearRegression()
    clf3.fit(df3.iloc[:, 2:-1], df3.iloc[:, 0])
    pred = clf3.predict(df3.iloc[:, 2:-1])
    value3 = mean_squared_error(df3.iloc[:, 0], pred)
    clf4 = LinearRegression()
    clf4.fit(df3.iloc[:, 2:], df3.iloc[:, 0])
    pred = clf4.predict(df3.iloc[:, 2:])
    value4 = mean_squared_error(df3.iloc[:, 0], pred)

    df2 = df.loc[df['CONTACT.TYPE'] == m]
    df2 = df2.groupby(['START.DATE'])['Contacts'].sum()
    df2 = pd.DataFrame(df2)
    df2.columns = ["Contacts"]
    df2["Date"] = df2.index
    df2["Index"] = 0
    for x in range(0, len(df2)):
        for y in range(0, len(dfi)):
            if df2.index[x] == dfi.index[y]:
                df2.iloc[x, 2] = dfi.iloc[y, 1]
    df2["IndexSq"] = df2["Index"] ** 2
    clf5 = LinearRegression()
    clf5.fit(df2.iloc[:, 2:-1], df2.iloc[:, 0])
    pred = clf5.predict(df2.iloc[:, 2:-1])
    value5 = mean_squared_error(df2.iloc[:, 0], pred)
    clf6 = LinearRegression()
    clf6.fit(df2.iloc[:, 2:], df2.iloc[:, 0])
    pred = clf6.predict(df2.iloc[:, 2:])
    value6 = mean_squared_error(df2.iloc[:, 0], pred)

    tracker.iloc[s,0], tracker.iloc[s, 1], tracker.iloc[s, 2], tracker.iloc[s, 3], tracker.iloc[s,4], tracker.iloc[s, 5], tracker.iloc[s, 6], tracker.iloc[s, 7] = m, n, str(value1), str(value2), str(value3), str(value4), str(value5), str(value6)
    s = s + 1

    b = min(value1,value2,value3,value4,value5,value6)
    if value1 == b:
        for i in range(0, len(dft)):
            if dft.iloc[i, 1] == m:
                dft.iloc[i, 2] = clf1.predict(dft.iloc[i, 6:18])
    elif value2 == b:
        for i in range(0, len(dft)):
            if dft.iloc[i, 1] == m:
                dft.iloc[i, 2] = clf2.predict(dft.iloc[i, 6:19])
    elif value3 == b:
        for i in range(0, len(dft)):
            if dft.iloc[i, 1] == m:
                dft.iloc[i, 2] = clf3.predict(dft.iloc[i, 19:23])
    elif value4 == b:
        for i in range(0, len(dft)):
            if dft.iloc[i, 1] == m:
                dft.iloc[i, 2] = clf4.predict(dft.iloc[i, 19:24])
    elif value5 == b:
        for i in range(0, len(dft)):
            if dft.iloc[i, 1] == m:
                dft.iloc[i, 2] = clf5.predict(dft.iloc[i, 4])
    elif value6 == b:
        for i in range(0, len(dft)):
            if dft.iloc[i, 1] == m:
                dft.iloc[i, 2] = clf6.predict(dft.iloc[i, 4:6])

dft.to_csv('ContactsOutput1.csv', index= False)
tracker.to_csv('ContactsTracker1.csv', index= False)

tracker = pd.read_csv('raka.csv')
s = 1

dft = pd.read_csv('Resolution2017.csv')
dft.iloc[:, 0] = dft.iloc[:, 0].str.replace('/\d/\d\d\d\d', '')
dft.iloc[:, 0] = dft.iloc[:, 0].str.replace('/\d\d/\d\d\d\d', '')
dft["IndexSq"] = dft["Index"]**3
dft["Index1"] = dft["Index"]
dft["Jan"] = 0
dft["Feb"] = 0
dft["Mar"] = 0
dft["Apr"] = 0
dft["May"] = 0
dft["Jun"] = 0
dft["Jul"] = 0
dft["Aug"] = 0
dft["Sep"] = 0
dft["Oct"] = 0
dft["Nov"] = 0
dft["IndexSq1"] = dft["Index"]**3
dft["Index2"] = dft["Index"]
dft["Q1"] = 1
dft["Q2"] = 0
dft["Q3"] = 0
dft["IndexSq2"] = dft["Index"]**3
for i in range(0, len(dft)):
    if dft.iloc[i, 0] == '1':
        dft.iloc[i, 8] = 1
    elif dft.iloc[i, 0] == '2':
        dft.iloc[i, 9] = 1
    elif dft.iloc[i, 0] == '3':
        dft.iloc[i, 10] = 1

df = pd.read_csv('Resolution_Pre_2017.csv')
for m in ('Commercial Claim','Consultation','Non Compliance', 'Request', 'Tecnical Claim'):
    for n in ('-','Appointment','Billing cycle','Business Cycle','Charter Commitments', 'Closing Application',
              'Complain','Contractual conditions','Customer Care','Customer Data Modification','Damage',
              'Data Protection and Comunic.Publi.','Defective installation','Duplicate Documents','Escape',
               'Facilities', 'GDPR','Infrastructures','Invoice Modifications','Invoice charges',
                'Invoiced consumption', 'Lack of pressure', 'Mod. Commercial Data',
                'Modifications Payments / Collections', 'Offer acceptance',
                'Official Complaint', 'Others','Paving','Payment',
              'Quality service','Service point trading','Sewerage','Smart Metering','Supplies','Technical management',
              'Water is missing','Water quality'):
        df1 = df.loc[(df['Category'] == m) & (df['Subject'] == n)]
        if len(df1) != 0:
            df1 = df1.groupby(['Date'])['Resolution'].sum()
            df1 = pd.DataFrame(df1)
            df1.columns = ["Resolution"]
            df1["Date"] = df1.index
            df1["Index"] = 0
            for x in range(0, len(df1)):
                for y in range(0, len(dfi)):
                    if df1.index[x] == dfi.index[y]:
                        df1.iloc[x, 2] = dfi.iloc[y, 1]
            df1["Jan"] = 0
            df1["Feb"] = 0
            df1["Mar"] = 0
            df1["Apr"] = 0
            df1["May"] = 0
            df1["Jun"] = 0
            df1["Jul"] = 0
            df1["Aug"] = 0
            df1["Sep"] = 0
            df1["Oct"] = 0
            df1["Nov"] = 0
            for x in range(0, len(df1)):
                df1.iloc[x, 1] = df1.iloc[x, 1][:7]
            for i in range(0, len(df1)):
                if str(df1.iloc[i, 1]).find('-01') != -1:
                    df1.iloc[i, 3] = 1
                if str(df1.iloc[i, 1]).find('-02') != -1:
                    df1.iloc[i, 4] = 1
                if str(df1.iloc[i, 1]).find('-03') != -1:
                    df1.iloc[i, 5] = 1
                if str(df1.iloc[i, 1]).find('-04') != -1:
                    df1.iloc[i, 6] = 1
                if str(df1.iloc[i, 1]).find('-05') != -1:
                    df1.iloc[i, 7] = 1
                if str(df1.iloc[i, 1]).find('-06') != -1:
                    df1.iloc[i, 8] = 1
                if str(df1.iloc[i, 1]).find('-07') != -1:
                    df1.iloc[i, 9] = 1
                if str(df1.iloc[i, 1]).find('-08') != -1:
                    df1.iloc[i, 10] = 1
                if str(df1.iloc[i, 1]).find('-09') != -1:
                    df1.iloc[i, 11] = 1
                if str(df1.iloc[i, 1]).find('-10') != -1:
                    df1.iloc[i, 12] = 1
                if str(df1.iloc[i, 1]).find('-11') != -1:
                    df1.iloc[i, 13] = 1
            df1["IndexSq"] = df1["Index"] ** 3
            clf2.fit(df1.iloc[:, 2:], df1.iloc[:, 0])
            pred = clf2.predict(df1.iloc[:, 2:])
            value2 = mean_squared_error(df1.iloc[:, 0], pred)

            df3 = df.loc[(df['Category'] == m) & (df['Subject'] == n)]
            df3 = df3.groupby(['Date'])['Resolution'].sum()
            df3 = pd.DataFrame(df3)
            df3.columns = ["Contacts"]
            df3["Date"] = df3.index
            df3["Index"] = 0
            for x in range(0, len(df3)):
                for y in range(0, len(dfi)):
                    if df3.index[x] == dfi.index[y]:
                        df3.iloc[x, 2] = dfi.iloc[y, 1]
            for i in range(0, len(df3)):
                df3.iloc[i, 1] = df3.iloc[i, 1][:7]
            df3["Q1"] = 0
            df3["Q2"] = 0
            df3["Q3"] = 0
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-02', '-01')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-03', '-01')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-04', '-02')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-05', '-02')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-06', '-02')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-07', '-03')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-08', '-03')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-09', '-03')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-10', '-04')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-11', '-04')
            df3.iloc[:, 1] = df3.iloc[:, 1].str.replace('-12', '-04')
            for i in range(0, len(df3)):
                if str(df3.iloc[i, 1]).find('-01') != -1:
                    df3.iloc[i, 3] = 1
                if str(df3.iloc[i, 1]).find('-02') != -1:
                    df3.iloc[i, 4] = 1
                if str(df3.iloc[i, 1]).find('-03') != -1:
                    df3.iloc[i, 5] = 1
            df3["IndexSq"] = df3["Index"] ** 3
            clf3 = LinearRegression()
            clf3.fit(df3.iloc[:, 2:-1], df3.iloc[:, 0])
            pred = clf3.predict(df3.iloc[:, 2:-1])
            value3 = mean_squared_error(df3.iloc[:, 0], pred)
            clf4 = LinearRegression()
            clf4.fit(df3.iloc[:, 2:], df3.iloc[:, 0])
            pred = clf4.predict(df3.iloc[:, 2:])
            value4 = mean_squared_error(df3.iloc[:, 0], pred)

            df2 = df.loc[(df['Category'] == m) & (df['Subject'] == n)]
            df2 = df2.groupby(['Date'])['Resolution'].sum()
            df2 = pd.DataFrame(df2)
            df2.columns = ["Contacts"]
            df2["Date"] = df2.index
            df2["Index"] = 0
            for x in range(0, len(df2)):
                for y in range(0, len(dfi)):
                    if df2.index[x] == dfi.index[y]:
                        df2.iloc[x, 2] = dfi.iloc[y, 1]
            df2["IndexSq"] = df2["Index"] ** 3
            clf5 = LinearRegression()
            clf5.fit(df2.iloc[:, 2:-1], df2.iloc[:, 0])
            pred = clf5.predict(df2.iloc[:, 2:-1])
            value5 = mean_squared_error(df2.iloc[:, 0], pred)
            clf6 = LinearRegression()
            clf6.fit(df2.iloc[:, 2:], df2.iloc[:, 0])
            pred = clf6.predict(df2.iloc[:, 2:])
            value6 = mean_squared_error(df2.iloc[:, 0], pred)

            tracker.iloc[s, 0], tracker.iloc[s, 1], tracker.iloc[s, 2], tracker.iloc[s, 3], tracker.iloc[s, 4], \
            tracker.iloc[s, 5], tracker.iloc[s, 6], tracker.iloc[s, 7] = m, n, str(value1), str(value2), str(
                value3), str(value4), str(value5), str(value6)
            s = s + 1

            b = min(value1, value2, value3, value4, value5, value6)
            if value1 == b:
                for i in range(0, len(dft)):
                    if dft.iloc[i, 1] == m and dft.iloc[i, 2] == n:
                        dft.iloc[i, 3] = clf1.predict(dft.iloc[i, 7:19])
            elif value2 == b:
                for i in range(0, len(dft)):
                    if dft.iloc[i, 1] == m and dft.iloc[i, 2] == n:
                        dft.iloc[i, 3] = clf2.predict(dft.iloc[i, 7:20])
            elif value3 == b:
                for i in range(0, len(dft)):
                    if dft.iloc[i, 1] == m and dft.iloc[i, 2] == n:
                        dft.iloc[i, 3] = clf3.predict(dft.iloc[i, 20:24])
            elif value4 == b:
                for i in range(0, len(dft)):
                    if dft.iloc[i, 1] == m and dft.iloc[i, 2] == n:
                        dft.iloc[i, 3] = clf4.predict(dft.iloc[i, 20:25])
            elif value5 == b:
                for i in range(0, len(dft)):
                    if dft.iloc[i, 1] == m and dft.iloc[i, 2] == n:
                        dft.iloc[i, 3] = clf5.predict(dft.iloc[i, 5])
            elif value6 == b:
                for i in range(0, len(dft)):
                    if dft.iloc[i, 1] == m and dft.iloc[i, 2] == n:
                        dft.iloc[i, 3] = clf6.predict(dft.iloc[i, 5:7])

dft.to_csv('ResolutionOutput1.csv', index= False)
tracker.to_csv('ResolutionTracker1.csv', index= False)
