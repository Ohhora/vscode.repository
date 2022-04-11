import quandl
my_quandl_key = 'mfzscyrD3nwwRm4F_xq7'
quandl.ApiConfig.api_key = my_quandl_key

# Oil price
oil_data = quandl.get('EIA/PET_RWTC_D')
#print(oil_data)

# Gold price
gold_data = quandl.get(dataset='LBMA/GOLD', start_date='2010-01-01', end_data='2020-12-31')
#print(gold_data.head())

# Silver price
silver_data = quandl.get(dataset='LBMA/SILVER', start_date='2020-01-01',end_date='202-01-01')

# Cu price
cu_data = quandl.get(dataset='CHRIS/CME_HG10', start_date='2010-01-01', end_date='2020-12-31')
print(cu_data.head())
