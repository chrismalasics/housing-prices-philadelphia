def get_data(soup):
    listing_data = {}
    soup_to_str = str(soup)
    
    try:
        street_address = (soup.find('span', itemprop="streetAddress")).text
    except:
        street_address = ('Not Found')
    address_locality = (soup.find('span', itemprop="addressLocality")).text
    address_region = (soup.find('span', itemprop="addressRegion")).text
    postal_code = (soup.find('span', itemprop="postalCode")).text

    price = re.findall(r'(?<=Last Sold for \$)\d{0,3},{0,1}\d{1,3},{0,1}\d{1,3}', soup_to_str)
    days_on_market = re.findall(r'(\d{1,3})[\s]*</div>\n<span>Days on market', soup_to_str)
    sqft_house = re.findall(r'(\d{0,2},{0,1}\d{3})</span>[<>\s\/A-z]+sq\sft',soup_to_str)
    sqft_lot = re.findall(r'lot_size":([\d.]+[^,])', soup_to_str)
    full_bath = re.findall(r'Full\s{1}Bathrooms:\s{1}(\d{1,2})',soup_to_str)
    half_bath = re.findall(r'1\/2\sBathrooms:([0-9\s]+[^<])',soup_to_str)
    bedrooms = re.findall(r'Bedrooms:\s{1}(\d{1,2})',soup_to_str)
    garage = re.findall(r'Garage\sSpaces:([\d\s]+[^<])', soup_to_str)
    master_bath = re.findall(r'Master\sBath(s):\s([A-Z\s]+[^<])', soup_to_str)

    cooling = re.findall(r'Cooling\sFeatures:(\s[A-z\s\/\(\)]+[^<])', soup_to_str)
    heating = re.findall(r'Heating\sFeatures:(\s[A-z\s\/\(\)]+[^<])', soup_to_str)

    annual_tax = re.findall(r'Annual Tax Amount:\s(\d{1,6}).', soup_to_str)
    house_type = re.findall(r'Structure\sType:([\sA-z\/-]+[^<])',soup_to_str)
    built = re.findall(r'[Bb]uilt:(\s+\d+)', soup_to_str)
    updated = re.findall(r'Date\supdated:([0-9\s\/]+[^<])', soup_to_str)

    neighborhood = re.findall(r'Source Neighborhood: ([A-z\s]*)', soup_to_str)
    neighborhood_median_sales = re.findall(r'(\d{0,3},{0,1}\d{0,3},{0,1}\d{0,3})[\D]*Median Sales Price', soup_to_str)
    neighborhood_median_days_on_market = re.findall(r'(\d{1,3})[\D]*Median Days on Market', soup_to_str)
    neighborhood_price_SQFT = re.findall(r'(\d{0,3},{0,1}\d{0,3})[\D]*Price Per Sq Ft', soup_to_str)
    association = re.findall(r'Association: ([A-z]{2,3})', soup_to_str)
    association_monthly = re.findall(r'Monthly Association Fees:\s(\d{1,5})', soup_to_str)

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
                    'Association Monthly': association_monthly}
    
    return listing_data