import os
from bs4 import BeautifulSoup

def generate_battery_report():
    os.system('powercfg /batteryreport /output battery_report.html')
    with open("battery_report.html", "r") as file:
        data = file.read()
    return data

def extract_battery_health(data):
    soup = BeautifulSoup(data, 'html.parser')
    
    # using bs4 to search the battery data in the parsed HTML
    try:
        DESIGN_CAPACITY = soup.find(text="DESIGN CAPACITY").find_next('td').text
        FULL_CHARGE_CAPACITY = soup.find(text="FULL CHARGE CAPACITY").find_next('td').text
    except AttributeError:
        print("Failed to extract data. Please check the structure of the --Battery_Report.html-- report.")
        return None

    print(f"DESIGN CAPACITY: {DESIGN_CAPACITY}")
    print(f"FULL CHARGE CAPACITY: {FULL_CHARGE_CAPACITY}")
    
    # Removing the mWh
    try:
        DESIGN_CAPACITY = int(DESIGN_CAPACITY.replace(' mWh', '').replace(',', ''))
        FULL_CHARGE_CAPACITY = int(FULL_CHARGE_CAPACITY.replace(' mWh', '').replace(',', ''))
    except ValueError:
        print("Failed to convert capacity values.")
        return None
    
    wear_level = 100 - (FULL_CHARGE_CAPACITY / DESIGN_CAPACITY) * 100
    return wear_level

if __name__ == "__main__":
    report_data = generate_battery_report()
    wear_level = extract_battery_health(report_data)
    if wear_level:
        print(f"Current Battery Wear Level: {wear_level:.2f}%")
    else:
        print("Unable to extract battery health information.")
