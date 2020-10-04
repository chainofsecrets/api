# swagger_client.SupplyApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supply_total_denomination_get**](SupplyApi.md#supply_total_denomination_get) | **GET** /supply/total/{denomination} | Total supply of a single coin denomination
[**supply_total_get**](SupplyApi.md#supply_total_get) | **GET** /supply/total | Total supply of coins in the chain


# **supply_total_denomination_get**
> str supply_total_denomination_get(denomination)

Total supply of a single coin denomination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplyApi()
denomination = 'denomination_example' # str | Coin denomination

try:
    # Total supply of a single coin denomination
    api_response = api_instance.supply_total_denomination_get(denomination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplyApi->supply_total_denomination_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denomination** | **str**| Coin denomination | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **supply_total_get**
> Supply supply_total_get()

Total supply of coins in the chain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplyApi()

try:
    # Total supply of coins in the chain
    api_response = api_instance.supply_total_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplyApi->supply_total_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Supply**](Supply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

