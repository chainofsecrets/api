# swagger_client.GovernanceApi

All URIs are relative to *https://api.secretapi.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gov_parameters_deposit_get**](GovernanceApi.md#gov_parameters_deposit_get) | **GET** /gov/parameters/deposit | Query governance deposit parameters
[**gov_parameters_tallying_get**](GovernanceApi.md#gov_parameters_tallying_get) | **GET** /gov/parameters/tallying | Query governance tally parameters
[**gov_parameters_voting_get**](GovernanceApi.md#gov_parameters_voting_get) | **GET** /gov/parameters/voting | Query governance voting parameters
[**gov_proposals_get**](GovernanceApi.md#gov_proposals_get) | **GET** /gov/proposals | Query proposals
[**gov_proposals_param_change_post**](GovernanceApi.md#gov_proposals_param_change_post) | **POST** /gov/proposals/param_change | Generate a parameter change proposal transaction
[**gov_proposals_post**](GovernanceApi.md#gov_proposals_post) | **POST** /gov/proposals | Submit a proposal
[**gov_proposals_proposal_id_deposits_depositor_get**](GovernanceApi.md#gov_proposals_proposal_id_deposits_depositor_get) | **GET** /gov/proposals/{proposalId}/deposits/{depositor} | Query deposit
[**gov_proposals_proposal_id_deposits_get**](GovernanceApi.md#gov_proposals_proposal_id_deposits_get) | **GET** /gov/proposals/{proposalId}/deposits | Query deposits
[**gov_proposals_proposal_id_deposits_post**](GovernanceApi.md#gov_proposals_proposal_id_deposits_post) | **POST** /gov/proposals/{proposalId}/deposits | Deposit tokens to a proposal
[**gov_proposals_proposal_id_get**](GovernanceApi.md#gov_proposals_proposal_id_get) | **GET** /gov/proposals/{proposalId} | Query a proposal
[**gov_proposals_proposal_id_proposer_get**](GovernanceApi.md#gov_proposals_proposal_id_proposer_get) | **GET** /gov/proposals/{proposalId}/proposer | Query proposer
[**gov_proposals_proposal_id_tally_get**](GovernanceApi.md#gov_proposals_proposal_id_tally_get) | **GET** /gov/proposals/{proposalId}/tally | Get a proposal&#39;s tally result at the current time
[**gov_proposals_proposal_id_votes_get**](GovernanceApi.md#gov_proposals_proposal_id_votes_get) | **GET** /gov/proposals/{proposalId}/votes | Query voters
[**gov_proposals_proposal_id_votes_post**](GovernanceApi.md#gov_proposals_proposal_id_votes_post) | **POST** /gov/proposals/{proposalId}/votes | Vote a proposal
[**gov_proposals_proposal_id_votes_voter_get**](GovernanceApi.md#gov_proposals_proposal_id_votes_voter_get) | **GET** /gov/proposals/{proposalId}/votes/{voter} | Query vote


# **gov_parameters_deposit_get**
> InlineResponse2008 gov_parameters_deposit_get()

Query governance deposit parameters

Query governance deposit parameters. The max_deposit_period units are in nanoseconds.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()

try:
    # Query governance deposit parameters
    api_response = api_instance.gov_parameters_deposit_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_parameters_deposit_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_parameters_tallying_get**
> object gov_parameters_tallying_get()

Query governance tally parameters

Query governance tally parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()

try:
    # Query governance tally parameters
    api_response = api_instance.gov_parameters_tallying_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_parameters_tallying_get: %s\n" % e)
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

# **gov_parameters_voting_get**
> object gov_parameters_voting_get()

Query governance voting parameters

Query governance voting parameters. The voting_period units are in nanoseconds.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()

try:
    # Query governance voting parameters
    api_response = api_instance.gov_parameters_voting_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_parameters_voting_get: %s\n" % e)
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

# **gov_proposals_get**
> list[TextProposal] gov_proposals_get(voter=voter, depositor=depositor, status=status)

Query proposals

Query proposals information with parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
voter = 'voter_example' # str | voter address (optional)
depositor = 'depositor_example' # str | depositor address (optional)
status = 'status_example' # str | proposal status, valid values can be `\"deposit_period\"`, `\"voting_period\"`, `\"passed\"`, `\"rejected\"` (optional)

try:
    # Query proposals
    api_response = api_instance.gov_proposals_get(voter=voter, depositor=depositor, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voter** | **str**| voter address | [optional] 
 **depositor** | **str**| depositor address | [optional] 
 **status** | **str**| proposal status, valid values can be &#x60;\&quot;deposit_period\&quot;&#x60;, &#x60;\&quot;voting_period\&quot;&#x60;, &#x60;\&quot;passed\&quot;&#x60;, &#x60;\&quot;rejected\&quot;&#x60; | [optional] 

### Return type

[**list[TextProposal]**](TextProposal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_param_change_post**
> StdTx gov_proposals_param_change_post(post_proposal_body)

Generate a parameter change proposal transaction

Generate a parameter change proposal transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
post_proposal_body = swagger_client.PostProposalBody1() # PostProposalBody1 | The parameter change proposal body that contains all parameter changes

try:
    # Generate a parameter change proposal transaction
    api_response = api_instance.gov_proposals_param_change_post(post_proposal_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_param_change_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_proposal_body** | [**PostProposalBody1**](PostProposalBody1.md)| The parameter change proposal body that contains all parameter changes | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_post**
> StdTx gov_proposals_post(post_proposal_body)

Submit a proposal

Send transaction to submit a proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
post_proposal_body = swagger_client.PostProposalBody() # PostProposalBody | valid value of `\"proposal_type\"` can be `\"text\"`, `\"parameter_change\"`, `\"software_upgrade\"`

try:
    # Submit a proposal
    api_response = api_instance.gov_proposals_post(post_proposal_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_proposal_body** | [**PostProposalBody**](PostProposalBody.md)| valid value of &#x60;\&quot;proposal_type\&quot;&#x60; can be &#x60;\&quot;text\&quot;&#x60;, &#x60;\&quot;parameter_change\&quot;&#x60;, &#x60;\&quot;software_upgrade\&quot;&#x60; | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_deposits_depositor_get**
> Deposit gov_proposals_proposal_id_deposits_depositor_get(proposal_id, depositor)

Query deposit

Query deposit by proposalId and depositor address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | proposal id
depositor = 'depositor_example' # str | Bech32 depositor address

try:
    # Query deposit
    api_response = api_instance.gov_proposals_proposal_id_deposits_depositor_get(proposal_id, depositor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_deposits_depositor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **depositor** | **str**| Bech32 depositor address | 

### Return type

[**Deposit**](Deposit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_deposits_get**
> list[Deposit] gov_proposals_proposal_id_deposits_get(proposal_id)

Query deposits

Query deposits by proposalId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | 

try:
    # Query deposits
    api_response = api_instance.gov_proposals_proposal_id_deposits_get(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_deposits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**|  | 

### Return type

[**list[Deposit]**](Deposit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_deposits_post**
> StdTx gov_proposals_proposal_id_deposits_post(proposal_id, post_deposit_body)

Deposit tokens to a proposal

Send transaction to deposit tokens to a proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | proposal id
post_deposit_body = swagger_client.PostDepositBody() # PostDepositBody | 

try:
    # Deposit tokens to a proposal
    api_response = api_instance.gov_proposals_proposal_id_deposits_post(proposal_id, post_deposit_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_deposits_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **post_deposit_body** | [**PostDepositBody**](PostDepositBody.md)|  | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_get**
> TextProposal gov_proposals_proposal_id_get(proposal_id)

Query a proposal

Query a proposal by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | 

try:
    # Query a proposal
    api_response = api_instance.gov_proposals_proposal_id_get(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**|  | 

### Return type

[**TextProposal**](TextProposal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_proposer_get**
> Proposer gov_proposals_proposal_id_proposer_get(proposal_id)

Query proposer

Query for the proposer for a proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | 

try:
    # Query proposer
    api_response = api_instance.gov_proposals_proposal_id_proposer_get(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_proposer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**|  | 

### Return type

[**Proposer**](Proposer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_tally_get**
> TallyResult gov_proposals_proposal_id_tally_get(proposal_id)

Get a proposal's tally result at the current time

Gets a proposal's tally result at the current time. If the proposal is pending deposits (i.e status 'DepositPeriod') it returns an empty tally result.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | proposal id

try:
    # Get a proposal's tally result at the current time
    api_response = api_instance.gov_proposals_proposal_id_tally_get(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_tally_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 

### Return type

[**TallyResult**](TallyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_votes_get**
> list[Vote] gov_proposals_proposal_id_votes_get(proposal_id)

Query voters

Query voters information by proposalId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | proposal id

try:
    # Query voters
    api_response = api_instance.gov_proposals_proposal_id_votes_get(proposal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_votes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 

### Return type

[**list[Vote]**](Vote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_votes_post**
> StdTx gov_proposals_proposal_id_votes_post(proposal_id, post_vote_body)

Vote a proposal

Send transaction to vote a proposal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | proposal id
post_vote_body = swagger_client.PostVoteBody() # PostVoteBody | valid value of `\"option\"` field can be `\"yes\"`, `\"no\"`, `\"no_with_veto\"` and `\"abstain\"`

try:
    # Vote a proposal
    api_response = api_instance.gov_proposals_proposal_id_votes_post(proposal_id, post_vote_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_votes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **post_vote_body** | [**PostVoteBody**](PostVoteBody.md)| valid value of &#x60;\&quot;option\&quot;&#x60; field can be &#x60;\&quot;yes\&quot;&#x60;, &#x60;\&quot;no\&quot;&#x60;, &#x60;\&quot;no_with_veto\&quot;&#x60; and &#x60;\&quot;abstain\&quot;&#x60; | 

### Return type

[**StdTx**](StdTx.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gov_proposals_proposal_id_votes_voter_get**
> Vote gov_proposals_proposal_id_votes_voter_get(proposal_id, voter)

Query vote

Query vote information by proposal Id and voter address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GovernanceApi()
proposal_id = 'proposal_id_example' # str | proposal id
voter = 'voter_example' # str | Bech32 voter address

try:
    # Query vote
    api_response = api_instance.gov_proposals_proposal_id_votes_voter_get(proposal_id, voter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GovernanceApi->gov_proposals_proposal_id_votes_voter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proposal_id** | **str**| proposal id | 
 **voter** | **str**| Bech32 voter address | 

### Return type

[**Vote**](Vote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

