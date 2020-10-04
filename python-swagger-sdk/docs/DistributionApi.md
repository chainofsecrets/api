# swagger_client.DistributionApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distribution_community_pool_get**](DistributionApi.md#distribution_community_pool_get) | **GET** /distribution/community_pool | Community pool parameters
[**distribution_delegators_delegator_addr_rewards_get**](DistributionApi.md#distribution_delegators_delegator_addr_rewards_get) | **GET** /distribution/delegators/{delegatorAddr}/rewards | Get the total rewards balance from all delegations
[**distribution_delegators_delegator_addr_rewards_post**](DistributionApi.md#distribution_delegators_delegator_addr_rewards_post) | **POST** /distribution/delegators/{delegatorAddr}/rewards | Withdraw all the delegator&#39;s delegation rewards
[**distribution_delegators_delegator_addr_rewards_validator_addr_get**](DistributionApi.md#distribution_delegators_delegator_addr_rewards_validator_addr_get) | **GET** /distribution/delegators/{delegatorAddr}/rewards/{validatorAddr} | Query a delegation reward
[**distribution_delegators_delegator_addr_rewards_validator_addr_post**](DistributionApi.md#distribution_delegators_delegator_addr_rewards_validator_addr_post) | **POST** /distribution/delegators/{delegatorAddr}/rewards/{validatorAddr} | Withdraw a delegation reward
[**distribution_delegators_delegator_addr_withdraw_address_get**](DistributionApi.md#distribution_delegators_delegator_addr_withdraw_address_get) | **GET** /distribution/delegators/{delegatorAddr}/withdraw_address | Get the rewards withdrawal address
[**distribution_delegators_delegator_addr_withdraw_address_post**](DistributionApi.md#distribution_delegators_delegator_addr_withdraw_address_post) | **POST** /distribution/delegators/{delegatorAddr}/withdraw_address | Replace the rewards withdrawal address
[**distribution_parameters_get**](DistributionApi.md#distribution_parameters_get) | **GET** /distribution/parameters | Fee distribution parameters
[**distribution_validators_validator_addr_get**](DistributionApi.md#distribution_validators_validator_addr_get) | **GET** /distribution/validators/{validatorAddr} | Validator distribution information
[**distribution_validators_validator_addr_outstanding_rewards_get**](DistributionApi.md#distribution_validators_validator_addr_outstanding_rewards_get) | **GET** /distribution/validators/{validatorAddr}/outstanding_rewards | Fee distribution outstanding rewards of a single validator
[**distribution_validators_validator_addr_rewards_get**](DistributionApi.md#distribution_validators_validator_addr_rewards_get) | **GET** /distribution/validators/{validatorAddr}/rewards | Commission and self-delegation rewards of a single validator
[**distribution_validators_validator_addr_rewards_post**](DistributionApi.md#distribution_validators_validator_addr_rewards_post) | **POST** /distribution/validators/{validatorAddr}/rewards | Withdraw the validator&#39;s rewards


# **distribution_community_pool_get**
> list[Coin] distribution_community_pool_get()

Community pool parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()

try:
    # Community pool parameters
    api_response = api_instance.distribution_community_pool_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_community_pool_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Coin]**](Coin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_delegators_delegator_addr_rewards_get**
> DelegatorTotalRewards distribution_delegators_delegator_addr_rewards_get(delegator_addr)

Get the total rewards balance from all delegations

Get the sum of all the rewards earned by delegations by a single delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get the total rewards balance from all delegations
    api_response = api_instance.distribution_delegators_delegator_addr_rewards_get(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_delegators_delegator_addr_rewards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**DelegatorTotalRewards**](DelegatorTotalRewards.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_delegators_delegator_addr_rewards_post**
> StdTx distribution_delegators_delegator_addr_rewards_post(delegator_addr, withdraw_request_body=withdraw_request_body)

Withdraw all the delegator's delegation rewards

Withdraw all the delegator's delegation rewards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
withdraw_request_body = swagger_client.WithdrawRequestBody() # WithdrawRequestBody |  (optional)

try:
    # Withdraw all the delegator's delegation rewards
    api_response = api_instance.distribution_delegators_delegator_addr_rewards_post(delegator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_delegators_delegator_addr_rewards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **withdraw_request_body** | [**WithdrawRequestBody**](WithdrawRequestBody.md)|  | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_delegators_delegator_addr_rewards_validator_addr_get**
> list[Coin] distribution_delegators_delegator_addr_rewards_validator_addr_get(delegator_addr, validator_addr)

Query a delegation reward

Query a single delegation reward by a delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query a delegation reward
    api_response = api_instance.distribution_delegators_delegator_addr_rewards_validator_addr_get(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_delegators_delegator_addr_rewards_validator_addr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**list[Coin]**](Coin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_delegators_delegator_addr_rewards_validator_addr_post**
> StdTx distribution_delegators_delegator_addr_rewards_validator_addr_post(delegator_addr, validator_addr, withdraw_request_body=withdraw_request_body)

Withdraw a delegation reward

Withdraw a delegator's delegation reward from a single validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator
withdraw_request_body = swagger_client.WithdrawRequestBody1() # WithdrawRequestBody1 |  (optional)

try:
    # Withdraw a delegation reward
    api_response = api_instance.distribution_delegators_delegator_addr_rewards_validator_addr_post(delegator_addr, validator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_delegators_delegator_addr_rewards_validator_addr_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 
 **withdraw_request_body** | [**WithdrawRequestBody1**](WithdrawRequestBody1.md)|  | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_delegators_delegator_addr_withdraw_address_get**
> Address distribution_delegators_delegator_addr_withdraw_address_get(delegator_addr)

Get the rewards withdrawal address

Get the delegations' rewards withdrawal address. This is the address in which the user will receive the reward funds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get the rewards withdrawal address
    api_response = api_instance.distribution_delegators_delegator_addr_withdraw_address_get(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_delegators_delegator_addr_withdraw_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_delegators_delegator_addr_withdraw_address_post**
> StdTx distribution_delegators_delegator_addr_withdraw_address_post(delegator_addr, withdraw_request_body=withdraw_request_body)

Replace the rewards withdrawal address

Replace the delegations' rewards withdrawal address for a new one.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
withdraw_request_body = swagger_client.WithdrawRequestBody2() # WithdrawRequestBody2 |  (optional)

try:
    # Replace the rewards withdrawal address
    api_response = api_instance.distribution_delegators_delegator_addr_withdraw_address_post(delegator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_delegators_delegator_addr_withdraw_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **withdraw_request_body** | [**WithdrawRequestBody2**](WithdrawRequestBody2.md)|  | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_parameters_get**
> object distribution_parameters_get()

Fee distribution parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()

try:
    # Fee distribution parameters
    api_response = api_instance.distribution_parameters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_parameters_get: %s\n" % e)
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

# **distribution_validators_validator_addr_get**
> ValidatorDistInfo distribution_validators_validator_addr_get(validator_addr)

Validator distribution information

Query the distribution information of a single validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Validator distribution information
    api_response = api_instance.distribution_validators_validator_addr_get(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_validators_validator_addr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**ValidatorDistInfo**](ValidatorDistInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_validators_validator_addr_outstanding_rewards_get**
> list[Coin] distribution_validators_validator_addr_outstanding_rewards_get(validator_addr)

Fee distribution outstanding rewards of a single validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Fee distribution outstanding rewards of a single validator
    api_response = api_instance.distribution_validators_validator_addr_outstanding_rewards_get(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_validators_validator_addr_outstanding_rewards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**list[Coin]**](Coin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_validators_validator_addr_rewards_get**
> list[Coin] distribution_validators_validator_addr_rewards_get(validator_addr)

Commission and self-delegation rewards of a single validator

Query the commission and self-delegation rewards of validator.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Commission and self-delegation rewards of a single validator
    api_response = api_instance.distribution_validators_validator_addr_rewards_get(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_validators_validator_addr_rewards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**list[Coin]**](Coin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distribution_validators_validator_addr_rewards_post**
> StdTx distribution_validators_validator_addr_rewards_post(validator_addr, withdraw_request_body=withdraw_request_body)

Withdraw the validator's rewards

Withdraw the validator's self-delegation and commissions rewards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator
withdraw_request_body = swagger_client.WithdrawRequestBody3() # WithdrawRequestBody3 |  (optional)

try:
    # Withdraw the validator's rewards
    api_response = api_instance.distribution_validators_validator_addr_rewards_post(validator_addr, withdraw_request_body=withdraw_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->distribution_validators_validator_addr_rewards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 
 **withdraw_request_body** | [**WithdrawRequestBody3**](WithdrawRequestBody3.md)|  | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

