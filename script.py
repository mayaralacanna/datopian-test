import csv, urllib, pandas, sys

if sys.argv[1] == "month":
    fileUrl = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls"
    dateFormat = "01 %b %Y"
    fileName = "csv/result_month.csv"
else:
    fileUrl = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls"
    dateFormat = "%d %b %Y"
    fileName = "csv/result_day.csv"

xlsFile = "csv/content.xls"
urllib.request.urlretrieve(fileUrl, xlsFile)

data = pandas.read_excel(xlsFile, 'Data 1', header=None, skiprows=3)

date = data[0].tolist()
price = data[1].tolist()

f = open(fileName, 'w')
writer = csv.writer(f)
writer.writerow(('Date','Price'))

for i in range(len(date)):
    dateFormatted = date[i].to_pydatetime()
    writer.writerow((dateFormatted.strftime(dateFormat), price[i]))

f.close()