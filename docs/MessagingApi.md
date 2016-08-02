# swagger_client.MessagingApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_message_id_get**](MessagingApi.md#messages_message_id_get) | **GET** /messages/{messageId} | Retrive the status and details of a submitted message.
[**messages_message_id_put**](MessagingApi.md#messages_message_id_put) | **PUT** /messages/{messageId} | Update the status of a submitted message.
[**messages_post**](MessagingApi.md#messages_post) | **POST** /messages | Send one or more SMS or text to voice messages.


# **messages_message_id_get**
> Message messages_message_id_get(message_id, account=account)

Retrive the status and details of a submitted message.

Get the status and details of a previously submitted message

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
api_instance = swagger_client.MessagingApi()
message_id = 'message_id_example' # str | Unique identifier representing message that has been submitted
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # Retrive the status and details of a submitted message.
    api_response = api_instance.messages_message_id_get(message_id, account=account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->messages_message_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Unique identifier representing message that has been submitted | 
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_message_id_put**
> messages_message_id_put(message_id, status, account=account)

Update the status of a submitted message.

Update the status of a scheduled message to cancelled to prevent the message from being sent

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
api_instance = swagger_client.MessagingApi()
message_id = 'message_id_example' # str | Unique identifier representing message to be updated.
status = swagger_client.Status() # Status | New status for the message.
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # Update the status of a submitted message.
    api_instance.messages_message_id_put(message_id, status, account=account)
except ApiException as e:
    print "Exception when calling MessagingApi->messages_message_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Unique identifier representing message to be updated. | 
 **status** | [**Status**](Status.md)| New status for the message. | 
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

void (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_post**
> MessageList messages_post(messages, account=account)

Send one or more SMS or text to voice messages.

Submit one or more (up to 100 per request) SMS or text to voice messages to be sent to the destination address. - A callback URL can be included with each message to which MO and DR notifications will be pushed to via a HTTP POST request. - The content of the message can be a unicode string, up to 5000 characters long - A delivery report can be be requested with the message which will be pushed to a HTTP endpoint if specified, or available via the Check Reports endpoint. - The destination number should be specified in E.164 international format. For information on E.164, please refer to http://en.wikipedia.org/wiki/E.164 - The format specifies which format the message will be sent as, SMS or VOICE - If specified the source number included in the request will be shown as the source number for the message, this feature is not enabled by default, please contact MessageMedia for more information. - If a source number is specified, the type of source number may also be specified. - The message will be scheduled to be delivered in the future if the scheduled parameter is specified. - A message expiry timestamp can be provided, if the message is not delivered by this time, it will be discarded. - Metadata can be included with the message. Up to 5 key value pair strings can be included with each message. This metadata will be available in delivery reports and replies. 

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
api_instance = swagger_client.MessagingApi()
messages = swagger_client.Messages() # Messages | A list of messages to be sent.
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # Send one or more SMS or text to voice messages.
    api_response = api_instance.messages_post(messages, account=account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingApi->messages_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **messages** | [**Messages**](Messages.md)| A list of messages to be sent. | 
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

[**MessageList**](MessageList.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

