import pandas as pd
from pathlib import Path
import numpy as np
import requests
import json


class Data:
    def __init__(self):
        self._rate_df = None
        self._residential_prop_prices_df = None
        
    @property
    def rate_df(self):
        return self._rate_df
    
    @property
    def residential_prop_prices_df(self):
        return self._rate_df
    
    def get_data_csv(self, csv_path: Path, index_column: str=None, index_type: str=None) ->  pd.DataFrame:  
                
        df = pd.read_csv(csv_path)         
        
        return df
        
    
    def get_data_request(self, url: str):
        """
        get_data_request : 
        """
        response = requests.get(url)
        
        try:
            response = requests.get(url)               
            response.raise_for_status()

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)            
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)            
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)            
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
            
        
        df = None
            
        return response
            
    def load_residential_prop_df(self) -> pd.DataFrame :
        
#        reade house prices from csv  
        csv_path = "Resources/house_prices.csv"
        _residential_prop_prices_df = self.get_data_csv(Path(csv_path))
        
        return self._residential_prop_prices_df