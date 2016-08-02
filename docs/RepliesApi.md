# swagger_client.RepliesApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replies_confirmed_post**](RepliesApi.md#replies_confirmed_post) | **POST** /replies/confirmed | Confirm the receipt of replies.
[**replies_get**](RepliesApi.md#replies_get) | **GET** /replies | Check for unconfirmed replies.


# **replies_confirmed_post**
> replies_confirmed_post(reply_id, account=account)

Confirm the receipt of replies.

The confirm replies endpoint will update the specified replies as confirmed, confirmed replies will no longer be returned in check replies requests.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: hmac
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RepliesApi()
reply_id = swagger_client.ReplyId() # ReplyId | A list of reply IDs to mark as confirmed.
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # Confirm the receipt of replies.
    api_instance.replies_confirmed_post(reply_id, account=account)
except ApiException as e:
    print "Exception when calling RepliesApi->replies_confirmed_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_id** | [**ReplyId**](ReplyId.md)| A list of reply IDs to mark as confirmed. | 
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

void (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replies_get**
> Replies replies_get(account=account)

Check for unconfirmed replies.

The replies endpoint returns the first 100 reply messages that have been received and haven't been confirmed using the confirm replies endpoint.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: hmac
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RepliesApi()
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # Check for unconfirmed replies.
    api_response = api_instance.replies_get(account=account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RepliesApi->replies_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

[**Replies**](Replies.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

