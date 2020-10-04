# swagger_client.SecretNetworkRESTApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_info_get**](SecretNetworkRESTApi.md#node_info_get) | **GET** /node_info | The properties of the connected node


# **node_info_get**
> InlineResponse200 node_info_get()

The properties of the connected node

Information about the connected node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretNetworkRESTApi()

try:
    # The properties of the connected node
    api_response = api_instance.node_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretNetworkRESTApi->node_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

