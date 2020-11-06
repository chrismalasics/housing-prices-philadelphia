from datetime import datetime
import re

def get_data(soup, url):
    listing_data = {}
    soup_to_str = str(soup)
    
    try:
        street_address = str((soup.find('span', itemprop="streetAddress")).text)
    except:
        street_address = ('Not Found')
    
    try:
        address_locality = str((soup.find('span', itemprop="addressLocality")).text)
    except:
        address_locality = ('Not Found') 
    
    try:
        address_region = str((soup.find('span', itemprop="addressRegion")).text)
    except:
        address_region = ('Not Found')
        
    try:
        postal_code = str((soup.find('span', itemprop="postalCode")).text)
    except:
        postal_code = ('Not Found')
        
    try:
        price = re.findall(r'(?<=Last Sold for \$)\d{0,3},{0,1}\d{1,3},{0,1}\d{1,3}', soup_to_str)
        price = price[0]
    except:
        price = ('Not Found')
        
    try:
        days_on_market = re.findall(r'(\d{1,3})[\s]*</div>\n<span>Days on market', soup_to_str)
    except:
        days_on_market = ('Not Found')
        
    try:
        sqft_house = re.findall(r'(\d{0,2},{0,1}\d{3})</span>[<>\s\/A-z]+sq\sft',soup_to_str)
        sqft_house = sqft_house[0]
    except:
        sqft_house = ('Not Found')
        
    try:
        sqft_lot = re.findall(r'lot_size":([\d.]+[^,])', soup_to_str)
        sqft_lot = sqft_lot[0]
    except:
        sqft_lot = ('Not Found')
        
    try:
        full_bath = re.findall(r'"baths_full":\s*(\d{1,3})',soup_to_str)
    except:
        full_bath = ('Not Found')
        
    try:
        half_bath = re.findall(r'"baths_half":\s*(\d{1,3})',soup_to_str)
    except:
        half_bath = ('Not Found')
        
    try:
        bedrooms = re.findall(r'Bed[A-z]*:\s{1}(\d{1,2})',soup_to_str)
    except:
        bedrooms = ('Not Found')
        
    try:
        garage = re.findall(r'Garage\sSpaces:([\d\s]+[^<])', soup_to_str)
    except:
        garage = ('Not Found')
        
    try:
        master_bath = re.findall(r'Master\sBath(s):\s([A-Z\s]+[^<])', soup_to_str)
    except:
        master_bath = ('Not Found')
        
    try:
        cooling = re.findall(r'Cooling[A-z\s]*:\s([A-z\/\s,]*)', soup_to_str)
    except:
        cooling = ('Not Found')
        
    try:
        heating = re.findall(r'Heating[A-z\s]*:\s([A-z\/\s,]*)', soup_to_str)
    except:
        heating = ('Not Found')
        
    try:
        annual_tax = re.findall(r'Annual Tax Amount:\s(\d{1,6}).', soup_to_str)
    except:
        annual_tax = ('Not Found')
        
    try:
        house_type = re.findall(r'[StructureProperty]*\s[Tt]ype:([\sA-z\/-]+[^<])',soup_to_str)
    except:
        house_type = ('Not Found')
        
    try:
        built = re.findall(r'[Bb]uilt:(\s+\d+)', soup_to_str)
    except:
        built = ('Not Found')
        
    try:
        updated = re.findall(r'Date\supdated:([0-9\s\/]+[^<])', soup_to_str)
    except:
        updated = ('Not Found')
        
    #********************************#
    
    try:
        neighborhood = re.findall(r'>([A-z\s]*)<\/a>\s*neighborhood', soup_to_str)
    except:
        neighborhood = ('Not Found')
        
    try:
        neighborhood_median_sales = re.findall(r'(\d{0,3},{0,1}\d{0,3},{0,1}\d{0,3})[\D]*Median Sales Price', soup_to_str)
    except:
        neighborhood_median_sales = ('Not Found')
        
    try:
        neighborhood_median_days_on_market = re.findall(r'(\d{1,3})[\D]*Median Days on Market', soup_to_str)
    except:
        neighborhood_median_days_on_market = ('Not Found')
        
    try:
        neighborhood_price_SQFT = re.findall(r'(\d{0,3},{0,1}\d{0,3})[\D]*Price Per Sq Ft', soup_to_str)
    except:
        neighborhood_price_SQFT = ('Not Found')
        
    try:
        association = re.findall(r'Association: ([A-z]{2,3})', soup_to_str)
    except:
        association = ('Not Found')
        
    try:
        association_monthly = re.findall(r'Monthly Association Fees:\s(\d{1,5})', soup_to_str)
    except:
        association_monthly = ('Not Found')
        
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
                    'Updated': updated,
                    'Neighborhood': neighborhood,
                    'Neighborhood median sales': neighborhood_median_sales,
                    'Neighborhood Median DOM' : neighborhood_median_days_on_market,
                    'Neighborhood Price SQFT': neighborhood_price_SQFT,
                    'Association': association,
                    'Association Monthly': association_monthly,
                    'URL': url,
                    'crawl time': datetime.now()}
    
    return listing_data