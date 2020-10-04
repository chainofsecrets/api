# swagger_client.StakingApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**staking_delegators_delegator_addr_delegations_get**](StakingApi.md#staking_delegators_delegator_addr_delegations_get) | **GET** /staking/delegators/{delegatorAddr}/delegations | Get all delegations from a delegator
[**staking_delegators_delegator_addr_delegations_post**](StakingApi.md#staking_delegators_delegator_addr_delegations_post) | **POST** /staking/delegators/{delegatorAddr}/delegations | Submit delegation
[**staking_delegators_delegator_addr_delegations_validator_addr_get**](StakingApi.md#staking_delegators_delegator_addr_delegations_validator_addr_get) | **GET** /staking/delegators/{delegatorAddr}/delegations/{validatorAddr} | Query the current delegation between a delegator and a validator
[**staking_delegators_delegator_addr_redelegations_post**](StakingApi.md#staking_delegators_delegator_addr_redelegations_post) | **POST** /staking/delegators/{delegatorAddr}/redelegations | Submit a redelegation
[**staking_delegators_delegator_addr_unbonding_delegations_get**](StakingApi.md#staking_delegators_delegator_addr_unbonding_delegations_get) | **GET** /staking/delegators/{delegatorAddr}/unbonding_delegations | Get all unbonding delegations from a delegator
[**staking_delegators_delegator_addr_unbonding_delegations_post**](StakingApi.md#staking_delegators_delegator_addr_unbonding_delegations_post) | **POST** /staking/delegators/{delegatorAddr}/unbonding_delegations | Submit an unbonding delegation
[**staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get**](StakingApi.md#staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get) | **GET** /staking/delegators/{delegatorAddr}/unbonding_delegations/{validatorAddr} | Query all unbonding delegations between a delegator and a validator
[**staking_delegators_delegator_addr_validators_get**](StakingApi.md#staking_delegators_delegator_addr_validators_get) | **GET** /staking/delegators/{delegatorAddr}/validators | Query all validators that a delegator is bonded to
[**staking_delegators_delegator_addr_validators_validator_addr_get**](StakingApi.md#staking_delegators_delegator_addr_validators_validator_addr_get) | **GET** /staking/delegators/{delegatorAddr}/validators/{validatorAddr} | Query a validator that a delegator is bonded to
[**staking_parameters_get**](StakingApi.md#staking_parameters_get) | **GET** /staking/parameters | Get the current staking parameter values
[**staking_pool_get**](StakingApi.md#staking_pool_get) | **GET** /staking/pool | Get the current state of the staking pool
[**staking_redelegations_get**](StakingApi.md#staking_redelegations_get) | **GET** /staking/redelegations | Get all redelegations (filter by query params)
[**staking_validators_get**](StakingApi.md#staking_validators_get) | **GET** /staking/validators | Get all validator candidates. By default it returns only the bonded validators.
[**staking_validators_validator_addr_delegations_get**](StakingApi.md#staking_validators_validator_addr_delegations_get) | **GET** /staking/validators/{validatorAddr}/delegations | Get all delegations from a validator
[**staking_validators_validator_addr_get**](StakingApi.md#staking_validators_validator_addr_get) | **GET** /staking/validators/{validatorAddr} | Query the information from a single validator
[**staking_validators_validator_addr_unbonding_delegations_get**](StakingApi.md#staking_validators_validator_addr_unbonding_delegations_get) | **GET** /staking/validators/{validatorAddr}/unbonding_delegations | Get all unbonding delegations from a validator


# **staking_delegators_delegator_addr_delegations_get**
> list[Delegation] staking_delegators_delegator_addr_delegations_get(delegator_addr)

Get all delegations from a delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get all delegations from a delegator
    api_response = api_instance.staking_delegators_delegator_addr_delegations_get(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_delegations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**list[Delegation]**](Delegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_delegations_post**
> StdTx staking_delegators_delegator_addr_delegations_post(delegator_addr, delegation=delegation)

Submit delegation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
delegation = swagger_client.Delegation() # Delegation | The password of the account to remove from the KMS (optional)

try:
    # Submit delegation
    api_response = api_instance.staking_delegators_delegator_addr_delegations_post(delegator_addr, delegation=delegation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_delegations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **delegation** | [**Delegation**](Delegation.md)| The password of the account to remove from the KMS | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_delegations_validator_addr_get**
> Delegation staking_delegators_delegator_addr_delegations_validator_addr_get(delegator_addr, validator_addr)

Query the current delegation between a delegator and a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query the current delegation between a delegator and a validator
    api_response = api_instance.staking_delegators_delegator_addr_delegations_validator_addr_get(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_delegations_validator_addr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**Delegation**](Delegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_redelegations_post**
> StdTx staking_delegators_delegator_addr_redelegations_post(delegator_addr, delegation=delegation)

Submit a redelegation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
delegation = swagger_client.Delegation2() # Delegation2 | The sender and tx information (optional)

try:
    # Submit a redelegation
    api_response = api_instance.staking_delegators_delegator_addr_redelegations_post(delegator_addr, delegation=delegation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_redelegations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **delegation** | [**Delegation2**](Delegation2.md)| The sender and tx information | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_unbonding_delegations_get**
> list[UnbondingDelegation] staking_delegators_delegator_addr_unbonding_delegations_get(delegator_addr)

Get all unbonding delegations from a delegator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Get all unbonding delegations from a delegator
    api_response = api_instance.staking_delegators_delegator_addr_unbonding_delegations_get(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_unbonding_delegations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**list[UnbondingDelegation]**](UnbondingDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_unbonding_delegations_post**
> StdTx staking_delegators_delegator_addr_unbonding_delegations_post(delegator_addr, delegation=delegation)

Submit an unbonding delegation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
delegation = swagger_client.Delegation1() # Delegation1 | The password of the account to remove from the KMS (optional)

try:
    # Submit an unbonding delegation
    api_response = api_instance.staking_delegators_delegator_addr_unbonding_delegations_post(delegator_addr, delegation=delegation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_unbonding_delegations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **delegation** | [**Delegation1**](Delegation1.md)| The password of the account to remove from the KMS | [optional] 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get**
> UnbondingDelegationPair staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get(delegator_addr, validator_addr)

Query all unbonding delegations between a delegator and a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query all unbonding delegations between a delegator and a validator
    api_response = api_instance.staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**UnbondingDelegationPair**](UnbondingDelegationPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_validators_get**
> list[Validator] staking_delegators_delegator_addr_validators_get(delegator_addr)

Query all validators that a delegator is bonded to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator

try:
    # Query all validators that a delegator is bonded to
    api_response = api_instance.staking_delegators_delegator_addr_validators_get(delegator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_validators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 

### Return type

[**list[Validator]**](Validator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_delegators_delegator_addr_validators_validator_addr_get**
> Validator staking_delegators_delegator_addr_validators_validator_addr_get(delegator_addr, validator_addr)

Query a validator that a delegator is bonded to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator_addr = 'delegator_addr_example' # str | Bech32 AccAddress of Delegator
validator_addr = 'validator_addr_example' # str | Bech32 ValAddress of Delegator

try:
    # Query a validator that a delegator is bonded to
    api_response = api_instance.staking_delegators_delegator_addr_validators_validator_addr_get(delegator_addr, validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_delegators_delegator_addr_validators_validator_addr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator_addr** | **str**| Bech32 AccAddress of Delegator | 
 **validator_addr** | **str**| Bech32 ValAddress of Delegator | 

### Return type

[**Validator**](Validator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_parameters_get**
> InlineResponse2006 staking_parameters_get()

Get the current staking parameter values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()

try:
    # Get the current staking parameter values
    api_response = api_instance.staking_parameters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_parameters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_pool_get**
> InlineResponse2005 staking_pool_get()

Get the current state of the staking pool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()

try:
    # Get the current state of the staking pool
    api_response = api_instance.staking_pool_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_pool_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_redelegations_get**
> list[Redelegation] staking_redelegations_get(delegator=delegator, validator_from=validator_from, validator_to=validator_to)

Get all redelegations (filter by query params)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
delegator = 'delegator_example' # str | Bech32 AccAddress of Delegator (optional)
validator_from = 'validator_from_example' # str | Bech32 ValAddress of SrcValidator (optional)
validator_to = 'validator_to_example' # str | Bech32 ValAddress of DstValidator (optional)

try:
    # Get all redelegations (filter by query params)
    api_response = api_instance.staking_redelegations_get(delegator=delegator, validator_from=validator_from, validator_to=validator_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_redelegations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegator** | **str**| Bech32 AccAddress of Delegator | [optional] 
 **validator_from** | **str**| Bech32 ValAddress of SrcValidator | [optional] 
 **validator_to** | **str**| Bech32 ValAddress of DstValidator | [optional] 

### Return type

[**list[Redelegation]**](Redelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_validators_get**
> list[Validator] staking_validators_get(status=status, page=page, limit=limit)

Get all validator candidates. By default it returns only the bonded validators.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
status = 'status_example' # str | The validator bond status. Must be either 'bonded', 'unbonded', or 'unbonding'. (optional)
page = 56 # int | The page number. (optional)
limit = 56 # int | The maximum number of items per page. (optional)

try:
    # Get all validator candidates. By default it returns only the bonded validators.
    api_response = api_instance.staking_validators_get(status=status, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_validators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The validator bond status. Must be either &#39;bonded&#39;, &#39;unbonded&#39;, or &#39;unbonding&#39;. | [optional] 
 **page** | **int**| The page number. | [optional] 
 **limit** | **int**| The maximum number of items per page. | [optional] 

### Return type

[**list[Validator]**](Validator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_validators_validator_addr_delegations_get**
> list[Delegation] staking_validators_validator_addr_delegations_get(validator_addr)

Get all delegations from a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Get all delegations from a validator
    api_response = api_instance.staking_validators_validator_addr_delegations_get(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_validators_validator_addr_delegations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**list[Delegation]**](Delegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_validators_validator_addr_get**
> Validator staking_validators_validator_addr_get(validator_addr)

Query the information from a single validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Query the information from a single validator
    api_response = api_instance.staking_validators_validator_addr_get(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_validators_validator_addr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**Validator**](Validator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **staking_validators_validator_addr_unbonding_delegations_get**
> list[UnbondingDelegation] staking_validators_validator_addr_unbonding_delegations_get(validator_addr)

Get all unbonding delegations from a validator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StakingApi()
validator_addr = 'validator_addr_example' # str | Bech32 OperatorAddress of validator

try:
    # Get all unbonding delegations from a validator
    api_response = api_instance.staking_validators_validator_addr_unbonding_delegations_get(validator_addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->staking_validators_validator_addr_unbonding_delegations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_addr** | **str**| Bech32 OperatorAddress of validator | 

### Return type

[**list[UnbondingDelegation]**](UnbondingDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

