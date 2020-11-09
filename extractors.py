#BeautifulSoup extractors and pre-processing for listing data

from datetime import datetime
import numpy as np
import re

def get_data(soup, url):
    listing_data = {}
    soup_to_str = str(soup)
    
    try:
        street_address = str((soup.find('span', itemprop="streetAddress")).text)
    except:
        street_address = np.nan
    
    try:
        address_locality = str((soup.find('span', itemprop="addressLocality")).text)
    except:
        address_locality = np.nan 
    
    try:
        address_region = str((soup.find('span', itemprop="addressRegion")).text)
    except:
        address_region = np.nan
        
    try:
        postal_code = str((soup.find('span', itemprop="postalCode")).text)
    except:
        postal_code = np.nan
        
    try:
        price = re.findall(r'(?<=Last Sold for \$)\d{0,3},{0,1}\d{1,3},{0,1}\d{1,3}', soup_to_str)
        price = int(price[0].replace(',',''))
    except:
        price = np.nan
        
    try:
        days_on_market = re.findall(r'(\d{1,3})[\s]*</div>\n<span>Days on market', soup_to_str)
        if days_on_market == []:
            days_on_market = 0
        else:
            days_on_market = int(days_on_market[0].replace(',',''))
    except:
        days_on_market = np.nan
        
    try:
        sqft_house = re.findall(r'(\d{0,2},{0,1}\d{3})</span>[<>\s\/A-z]+sq\sft',soup_to_str)
        sqft_house = int(sqft_house[0].replace(',',''))
    except:
        sqft_house = np.nan
        
    try:
        sqft_lot = re.findall(r'lot_size":([\d.]+[^,])', soup_to_str)
        if sqft_lot == []:
            sqft_lot = 0
        else:
            sqft_lot = int(sqft_lot[0].replace(',',''))
    except:
        sqft_lot = np.nan
        
    try:
        full_bath = re.findall(r'"baths_full":\s*(\d{1,3})',soup_to_str)
        if full_bath == []:
            full_bath = 0
        else:
            full_bath = int(full_bath[0].replace(',',''))
    except:
        full_bath = np.nan
        
    try:
        half_bath = re.findall(r'"baths_half":\s*(\d{1,3})',soup_to_str)
        if half_bath == []:
            half_bath = 0
        else:
            half_bath = int(half_bath[0].replace(',',''))
    except:
        half_bath = np.nan
        
    try:
        bedrooms = re.findall(r'Bed[A-z]*:\s{1}(\d{1,2})',soup_to_str)
        bedrooms = int(bedrooms[0])
    except:
        bedrooms = np.nan
        
    try:
        garage = re.findall(r'Garage\sSpaces:([\d\s]+[^<])', soup_to_str)
        if garage == []:
            garage = 'No'
    except:
        garage = np.nan
        
    try:
        master_bath = re.findall(r'Master\sBath(s):\s([A-Z\s]+[^<])', soup_to_str)
        if master_bath == []:
            master_bath = 'No'
    except:
        master_bath = np.nan
        
    try:
        cooling = re.findall(r'Cooling[A-z\s]*:\s([A-z\/\s,]*)', soup_to_str)
        if cooling == []:
            cooling = 'No'
    except:
        cooling = np.nan
        
    try:
        heating = re.findall(r'Heating[A-z\s]*:\s([A-z\/\s,]*)', soup_to_str)
        if heating == []:
            heating = 'No'
    except:
        heating = np.nan
        
    try:
        #annual_tax = re.findall(r'Annual Tax Amount:\s(\d{1,6}).', soup_to_str)
        annual_tax = re.findall(r'Total Assessment[\D]*2020[\D]*\$(\d{0,3},{0,1}\d{1,3})<', soup_to_str)
        if annual_tax == []:
            annual_tax = 'Not Found'
        else:
            annual_tax = int(annual_tax[0].replace(',',''))
    except:
        annual_tax = np.nan
        
    try:
        house_type = re.findall(r'[StructureProperty]*\s[Tt]ype:([\sA-z\/-]+[^<])',soup_to_str)
    except:
        house_type = np.nan
        
    try:
        built = re.findall(r'[Bb]uilt:(\s+\d+)', soup_to_str)
        if built == []:
            built = 'Not Found'
        else:
            built = int(built[0].replace(',',''))
    except:
        built = np.nan
        
    try:
        updated = re.findall(r'Date\supdated:([0-9\s\/]+[^<])', soup_to_str)
        if updated == []:
            updated = 'Not Updated'
        else:
            date_str = updated[0].strip()
            date_time_obj = datetime.strptime(date_str, '%m/%d/%Y')
            updated = int(date_time_obj.year)
    except:
        updated = np.nan
        
    #********************************#
    
    try:
        neighborhood = re.findall(r'>([A-z\s]*)<\/a>\s*neighborhood', soup_to_str)
        if neighborhood == []:
            neighborhood = 'Not Found'
        else: 
            neighborhood = neighborhood[0]
    except:
        neighborhood = np.nan
        
    try:
        neighborhood_median_sales = re.findall(r'(\d{0,3},{0,1}\d{0,3},{0,1}\d{0,3})[\D]*Median Sales Price', soup_to_str)
        if neighborhood_median_sales == []:
            neighborhood_median_sales = 'Not Found'
        else:
            neighborhood_median_sales = int(neighborhood_median_sales[0].replace(',',''))
    except:
        neighborhood_median_sales = np.nan
        
    try:
        neighborhood_median_days_on_market = re.findall(r'(\d{1,3})[\D]*Median Days on Market', soup_to_str)
        if neighborhood_median_days_on_market == []:
            neighborhood_median_days_on_market = 'Not Found'
        else:
            neighborhood_median_days_on_market = int(neighborhood_median_days_on_market[0].replace(',',''))
    except:
        neighborhood_median_days_on_market = np.nan
        
    try:
        neighborhood_price_SQFT = re.findall(r'(\d{0,3},{0,1}\d{0,3})[\D]*Price Per Sq Ft', soup_to_str)
        if neighborhood_price_SQFT == []:
            neighborhood_price_SQFT = 'Not Found'
        else:
            neighborhood_price_SQFT = int(neighborhood_price_SQFT[0].replace(',',''))
    except:
        neighborhood_price_SQFT = np.nan
        
    try:
        association = re.findall(r'Association: ([A-z]{2,3})', soup_to_str)
        if association == []:
            association = 'No'
        else:
            association = association[0]
    except:
        association = np.nan
        
    try:
        association_monthly = re.findall(r'Monthly Association Fees:\s(\d{1,5})', soup_to_str)
        if association_monthly == []:
            association_monthly = 0
        else:
            association_monthly = int(association_monthly[0].replace(',',''))
    except:
        association_monthly = np.nan
        
    #********************************#   
        
    listing_data = {'Address': street_address,
                    'Locality': address_locality,
                    'Region': address_region,
                    'Postal Code': postal_code,
                    'Price': price,
                    'Days on Market': days_on_market,
                    'SQFT House': sqft_house,
                    'SQFT Lot': sqft_lot,
                    'Full Baths': full_bath,
                    'Half Baths': half_bath,
                    'Bedrooms': bedrooms,
                    'Garage': garage,
                    'Master Bath': master_bath,
                    'Cooling': cooling,
                    'Heating': heating,
                    'Annual Tax': annual_tax,
                    'House Type': house_type,
                    'Build Year': built,
                    'Remodel Year': updated,
                    'Neighborhood': neighborhood,
                    'Neighborhood median sales': neighborhood_median_sales,
                    'Neighborhood Median DOM' : neighborhood_median_days_on_market,
                    'Neighborhood Price SQFT': neighborhood_price_SQFT,
                    'Association': association,
                    'Association Monthly': association_monthly,
                    'URL': url,
                    'crawl time': datetime.now()}
    
    return listing_data