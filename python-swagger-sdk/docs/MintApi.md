# swagger_client.MintApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**minting_annual_provisions_get**](MintApi.md#minting_annual_provisions_get) | **GET** /minting/annual-provisions | Current minting annual provisions value
[**minting_inflation_get**](MintApi.md#minting_inflation_get) | **GET** /minting/inflation | Current minting inflation value
[**minting_parameters_get**](MintApi.md#minting_parameters_get) | **GET** /minting/parameters | Minting module parameters


# **minting_annual_provisions_get**
> str minting_annual_provisions_get()

Current minting annual provisions value

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MintApi()

try:
    # Current minting annual provisions value
    api_response = api_instance.minting_annual_provisions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MintApi->minting_annual_provisions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minting_inflation_get**
> str minting_inflation_get()

Current minting inflation value

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MintApi()

try:
    # Current minting inflation value
    api_response = api_instance.minting_inflation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MintApi->minting_inflation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minting_parameters_get**
> object minting_parameters_get()

Minting module parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MintApi()

try:
    # Minting module parameters
    api_response = api_instance.minting_parameters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MintApi->minting_parameters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

