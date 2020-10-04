# swagger_client.BankApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_accounts_address_transfers_post**](BankApi.md#bank_accounts_address_transfers_post) | **POST** /bank/accounts/{address}/transfers | Send coins from one account to another
[**bank_balances_address_get**](BankApi.md#bank_balances_address_get) | **GET** /bank/balances/{address} | Get the account balances


# **bank_accounts_address_transfers_post**
> StdTx bank_accounts_address_transfers_post(address, account)

Send coins from one account to another

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()
address = 'address_example' # str | Account address in bech32 format
account = swagger_client.Account() # Account | The sender and tx information

try:
    # Send coins from one account to another
    api_response = api_instance.bank_accounts_address_transfers_post(address, account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->bank_accounts_address_transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address in bech32 format | 
 **account** | [**Account**](Account.md)| The sender and tx information | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_balances_address_get**
> list[Coin] bank_balances_address_get(address)

Get the account balances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankApi()
address = 'address_example' # str | Account address in bech32 format

try:
    # Get the account balances
    api_response = api_instance.bank_balances_address_get(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankApi->bank_balances_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Account address in bech32 format | 

### Return type

[**list[Coin]**](Coin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

