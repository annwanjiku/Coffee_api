import requests
import csv
from openpyxl import workbook

from pprint import pprint

url = 'https://fake-coffee-api.vercel.app/api'
response = requests.get(url)
if response.status_code == 200:
    print("Fetch successful\n")
    results = response.json()
else:
    print("Fetch failed!")

# pprint(results)

ids = []
names = []
roast_levels = []
prices = []
weights = []
regions = []

for i in range(0, len(results)):
    id = results[i]["id"]
    ids.append(id)

    name = results[i]["name"]
    names.append(name)

    roast_level = results[i]["roast_level"]
    roast_levels.append(roast_level)

    weight = results[i]["weight"]
    weights.append(weight)

    description = results[i]["description"]

    price = results[i]["price"]
    prices.append(price)

    region = results[i]["region"]
    regions.append(region)

    print(f' Coffee Name: {name} \n Description: {description} \n Price: {price} \n Region: {region} \n ')
print(str(len(results)) + " Coffee types")

print("Prices: \n",prices)
average_price = (sum(prices) / len(prices))
print("Average price of the coffee's :{:.2f}\n".format(average_price))

print("Weights;\n",weights)

All_regions = []
for i in range(len(regions)):
    if regions[i] not in All_regions:
        All_regions.append( regions[i])

print("\nRegions that Coffee originates from : {}".format(All_regions))

with open("Coffee.csv", "w") as csv_file:
    fieldnames = ["ID", "Name", "Roast Level", "Price", "Weight", "Regions"]
    spreadsheet = csv.DictWriter(csv_file, fieldnames=fieldnames)

    spreadsheet.writeheader()
    for i in range(len(ids)):
        spreadsheet.writerow({
            "ID": ids[i],
            "Name": names[i],
            "Roast Level": roast_levels[i],
            "Price": prices[i],
            "Weight": weights[i],
            "Regions": regions[i],
        })

    print("\nData successfully written to csv!")

wb = workbook()
ws = wb.active

ws.append("ID", "Name", "Roast Level", "Price", "Weight", "Regions")

for i in range(len(ids)):
    ws.append([ids[i], names[i], roast_levels[i], prices[i], weights[i], regions[i]])

wb.save("Coffee.xlsx")

print("\nData successfully written to Excel file!")