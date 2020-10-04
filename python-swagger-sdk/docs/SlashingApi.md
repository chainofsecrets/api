# swagger_client.SlashingApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slashing_parameters_get**](SlashingApi.md#slashing_parameters_get) | **GET** /slashing/parameters | Get the current slashing parameters
[**slashing_signing_infos_get**](SlashingApi.md#slashing_signing_infos_get) | **GET** /slashing/signing_infos | Get sign info of given all validators
[**slashing_validators_validator_addr_unjail_post**](SlashingApi.md#slashing_validators_validator_addr_unjail_post) | **POST** /slashing/validators/{validatorAddr}/unjail | Unjail a jailed validator


# **slashing_parameters_get**
> InlineResponse2007 slashing_parameters_get()

Get the current slashing parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()

try:
    # Get the current slashing parameters
    api_response = api_instance.slashing_parameters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->slashing_parameters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slashing_signing_infos_get**
> list[SigningInfo] slashing_signing_infos_get(page, limit)

Get sign info of given all validators

Get sign info of all validators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()
page = 56 # int | Page number
limit = 56 # int | Maximum number of items per page

try:
    # Get sign info of given all validators
    api_response = api_instance.slashing_signing_infos_get(page, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->slashing_signing_infos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 
 **limit** | **int**| Maximum number of items per page | 

### Return type

[**list[SigningInfo]**](SigningInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slashing_validators_validator_addr_unjail_post**
> StdTx slashing_validators_validator_addr_unjail_post(validator_addr, unjail_body)

Unjail a jailed validator

Send transaction to unjail a jailed validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SlashingApi()
validator_addr = 'validator_addr_example' # str | Bech32 validator address
unjail_body = swagger_client.UnjailBody() # UnjailBody | 

try:
    # Unjail a jailed validator
    api_response = api_instance.slashing_validators_validator_addr_unjail_post(validator_addr, unjail_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlashingApi->slashing_validators_validator_addr_unjail_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 validator address | 
 **unjail_body** | [**UnjailBody**](UnjailBody.md)|  | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

