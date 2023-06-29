# Car-info-scrapping Program


## Goal of the project

Extract details on the prices of all the vehicles that have specific features, such as the brand, the lowest and highest prices, and the level of usage. Accordingly, each of these parameters can be altered in a single function in the code.

## Technologies used

* **Python**.
* **Beautiful Soup 4.**
* **Excel Spreadsheets.**
* **Pandas library.**

## Description of the scrapping process

The *Preparator* function receives all the parameters (the base URL, the minimum and maximum price, the brand, and the status), gathers them all into a single URL, and delivers it as a string.

The *GetData* function receives the output of the *Preparator* and uses it to retrieve the title and price of each automobile on the page before moving on to the next one until no more cars are left. The variable *AllCarsOutput* contains all the data.

The *SaveData* function is then executed, with the only parameter being the *AllCarsOutput* variable. This function completes the scrapping process by exporting all the data from the *AllCarsOutput* variable to an **Excel sheet** called *Cars List.xls*, using the **Pandas package**.
