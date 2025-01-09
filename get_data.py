import pandas as pd
import requests

def get_data_from_api(url, export=False):
    """
    Simple function to fetch data from an API and optionally save it to a CSV file.

    Parameters:
        url (str): Base URL of the API.
        export (bool): If True, saves the data to a CSV file.

    Returns:
        None
    """

    # Making the GET request
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Converting the response to JSON
        data = response.json()
        
        # Accessing the "items" key in the dictionary
        items = data.get("items", [])
        
        # Converting the data to a pandas DataFrame
        df = pd.DataFrame(items)
        
        if export:
            # Saving the data to a CSV file
            df.to_csv("dados_pvl.csv", index=False)
            print("Data saved in 'dados_pvl.csv'")

        return df
    
    else:
        print(f"Error: {response.status_code}")