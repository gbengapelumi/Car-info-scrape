from bs4 import BeautifulSoup
import requests
import pandas as pd

BaseUrl = '/www.cars.com/shopping/results/?'

# Function that prepares the URL with the parameters given by the client
def Preparator(BaseUrl, MaxPrice, MinPrice, brand, status):
    Url = BaseUrl + 'dealer_id=&keyword=&list_price_max=%s&list_price_min=%s&makes[]=%s&maximum_distance=30&mileage_max=&monthly_payment=3289&page_size=20&sort=best_match_desc&stock_type=%s&year_max=&year_min=&zip=60606' % (MaxPrice, MinPrice, brand, status)
    print(Url)
    return Url

AllCarsOutput = []

# Function to get the Cars' data, one by one and then store each one of them in the "AllCarsOutput" variable
def GetData(Url):
    url = Url
    while True:
        Req = requests.get('http:/' + url).text
        Soup = BeautifulSoup(Req, 'html.parser')
        CarList = Soup.find_all('div', class_='vehicle-details')
        PageBtns = Soup.find_all('a', class_='sds-button sds-button--secondary sds-pagination__control')
        print(PageBtns)
        NextPageBtn = []
        for i in PageBtns:
            if i['aria-label'] == 'Next page':
                NextPageBtn = i
                break
            else:
                pass
        for i in range(len(CarList)):
            CarListOutput = {
                'Title': CarList[i].find('h2', class_='title').text,
                'Price': CarList[i].find('span', class_='primary-price').text,
                'Stock-Type': CarList[i].find('p', class_ = 'stock-type').text,
            }
            AllCarsOutput.append(CarListOutput)
            print(CarListOutput)
            print(NextPageBtn)
        if NextPageBtn:
            url = '/www.cars.com' + NextPageBtn['href']
            pass
        else:
            break


# Function to export all the retrieved data into an .xls file
def SaveData(OP):
    df = pd.DataFrame(OP, columns=['Title', 'Price', 'Stock-Type'])
    df.to_excel('Cars List.xls', index=True, columns=['Title', 'Price', 'Stock-Type'])

# Run the whole process given certain parameters
FUrl = Preparator(BaseUrl, 175000, 2000, 'hyundai', 'all')
GetData(FUrl)
SaveData(AllCarsOutput)