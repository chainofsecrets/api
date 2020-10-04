# swagger_client.AuthApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_accounts_address_get**](AuthApi.md#auth_accounts_address_get) | **GET** /auth/accounts/{address} | Get the account information on blockchain


# **auth_accounts_address_get**
> InlineResponse2004 auth_accounts_address_get(address)

Get the account information on blockchain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
address = 'address_example' # str | Account address

try:
    # Get the account information on blockchain
    api_response = api_instance.auth_accounts_address_get(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_accounts_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

