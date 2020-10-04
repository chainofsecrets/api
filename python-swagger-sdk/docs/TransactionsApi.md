# swagger_client.TransactionsApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**txs_decode_post**](TransactionsApi.md#txs_decode_post) | **POST** /txs/decode | Decode a transaction from the Amino wire format
[**txs_encode_post**](TransactionsApi.md#txs_encode_post) | **POST** /txs/encode | Encode a transaction to the Amino wire format
[**txs_get**](TransactionsApi.md#txs_get) | **GET** /txs | Search transactions
[**txs_hash_get**](TransactionsApi.md#txs_hash_get) | **GET** /txs/{hash} | Get a Tx by hash
[**txs_post**](TransactionsApi.md#txs_post) | **POST** /txs | Broadcast a signed tx


# **txs_decode_post**
> StdTx txs_decode_post(tx)

Decode a transaction from the Amino wire format

Decode a transaction (signed or not) from base64-encoded Amino serialized bytes to JSON

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
tx = swagger_client.Tx1() # Tx1 | The tx to decode

try:
    # Decode a transaction from the Amino wire format
    api_response = api_instance.txs_decode_post(tx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->txs_decode_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx** | [**Tx1**](Tx1.md)| The tx to decode | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **txs_encode_post**
> InlineResponse2003 txs_encode_post(tx)

Encode a transaction to the Amino wire format

Encode a transaction (signed or not) from JSON to base64-encoded Amino serialized bytes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
tx = swagger_client.Tx() # Tx | The tx to encode

try:
    # Encode a transaction to the Amino wire format
    api_response = api_instance.txs_encode_post(tx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->txs_encode_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx** | [**Tx**](Tx.md)| The tx to encode | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **txs_get**
> PaginatedQueryTxs txs_get(message_action=message_action, message_sender=message_sender, page=page, limit=limit, tx_minheight=tx_minheight, tx_maxheight=tx_maxheight)

Search transactions

Search transactions by events.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
message_action = 'message_action_example' # str | transaction events such as 'message.action=send' which results in the following endpoint: 'GET /txs?message.action=send'. note that each module documents its own events. look for xx_events.md in the corresponding cosmos-sdk/docs/spec directory (optional)
message_sender = 'message_sender_example' # str | transaction tags with sender: 'GET /txs?message.action=send&message.sender=secret16xyempempp92x9hyzz9wrgf94r6j9h5f06pxxv' (optional)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number of items per page (optional)
tx_minheight = 56 # int | transactions on blocks with height greater or equal this value (optional)
tx_maxheight = 56 # int | transactions on blocks with height less than or equal this value (optional)

try:
    # Search transactions
    api_response = api_instance.txs_get(message_action=message_action, message_sender=message_sender, page=page, limit=limit, tx_minheight=tx_minheight, tx_maxheight=tx_maxheight)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->txs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_action** | **str**| transaction events such as &#39;message.action&#x3D;send&#39; which results in the following endpoint: &#39;GET /txs?message.action&#x3D;send&#39;. note that each module documents its own events. look for xx_events.md in the corresponding cosmos-sdk/docs/spec directory | [optional] 
 **message_sender** | **str**| transaction tags with sender: &#39;GET /txs?message.action&#x3D;send&amp;message.sender&#x3D;secret16xyempempp92x9hyzz9wrgf94r6j9h5f06pxxv&#39; | [optional] 
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number of items per page | [optional] 
 **tx_minheight** | **int**| transactions on blocks with height greater or equal this value | [optional] 
 **tx_maxheight** | **int**| transactions on blocks with height less than or equal this value | [optional] 

### Return type

[**PaginatedQueryTxs**](PaginatedQueryTxs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **txs_hash_get**
> TxQuery txs_hash_get(hash)

Get a Tx by hash

Retrieve a transaction using its hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
hash = 'hash_example' # str | Tx hash

try:
    # Get a Tx by hash
    api_response = api_instance.txs_hash_get(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->txs_hash_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Tx hash | 

### Return type

[**TxQuery**](TxQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **txs_post**
> BroadcastTxCommitResult txs_post(tx_broadcast)

Broadcast a signed tx

Broadcast a signed tx to a full node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
tx_broadcast = swagger_client.TxBroadcast() # TxBroadcast | The tx must be a signed StdTx. The supported broadcast modes include `\"block\"`(return after tx commit), `\"sync\"`(return afer CheckTx) and `\"async\"`(return right away).

try:
    # Broadcast a signed tx
    api_response = api_instance.txs_post(tx_broadcast)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->txs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_broadcast** | [**TxBroadcast**](TxBroadcast.md)| The tx must be a signed StdTx. The supported broadcast modes include &#x60;\&quot;block\&quot;&#x60;(return after tx commit), &#x60;\&quot;sync\&quot;&#x60;(return afer CheckTx) and &#x60;\&quot;async\&quot;&#x60;(return right away). | 

### Return type

[**BroadcastTxCommitResult**](BroadcastTxCommitResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

