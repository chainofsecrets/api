# swagger_client.TendermintRPCApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blocks_height_get**](TendermintRPCApi.md#blocks_height_get) | **GET** /blocks/{height} | Get a block at a certain height
[**blocks_latest_get**](TendermintRPCApi.md#blocks_latest_get) | **GET** /blocks/latest | Get the latest block
[**syncing_get**](TendermintRPCApi.md#syncing_get) | **GET** /syncing | Syncing state of node
[**validatorsets_height_get**](TendermintRPCApi.md#validatorsets_height_get) | **GET** /validatorsets/{height} | Get a validator set a certain height
[**validatorsets_latest_get**](TendermintRPCApi.md#validatorsets_latest_get) | **GET** /validatorsets/latest | Get the latest validator set


# **blocks_height_get**
> BlockQuery blocks_height_get(height)

Get a block at a certain height

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintRPCApi()
height = 8.14 # float | Block height

try:
    # Get a block at a certain height
    api_response = api_instance.blocks_height_get(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintRPCApi->blocks_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **float**| Block height | 

### Return type

[**BlockQuery**](BlockQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks_latest_get**
> BlockQuery blocks_latest_get()

Get the latest block

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintRPCApi()

try:
    # Get the latest block
    api_response = api_instance.blocks_latest_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintRPCApi->blocks_latest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockQuery**](BlockQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **syncing_get**
> InlineResponse2001 syncing_get()

Syncing state of node

Get if the node is currently syning with other nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintRPCApi()

try:
    # Syncing state of node
    api_response = api_instance.syncing_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintRPCApi->syncing_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validatorsets_height_get**
> InlineResponse2002 validatorsets_height_get(height)

Get a validator set a certain height

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintRPCApi()
height = 8.14 # float | Block height

try:
    # Get a validator set a certain height
    api_response = api_instance.validatorsets_height_get(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintRPCApi->validatorsets_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **float**| Block height | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validatorsets_latest_get**
> InlineResponse2002 validatorsets_latest_get()

Get the latest validator set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TendermintRPCApi()

try:
    # Get the latest validator set
    api_response = api_instance.validatorsets_latest_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TendermintRPCApi->validatorsets_latest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

