# swagger_client.DeliveryReportsApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delivery_reports_confirmed_post**](DeliveryReportsApi.md#delivery_reports_confirmed_post) | **POST** /delivery_reports/confirmed | Confirm the receipt of delivery reports.
[**delivery_reports_get**](DeliveryReportsApi.md#delivery_reports_get) | **GET** /delivery_reports | This endpoint is used to check for unconfirmed reports.


# **delivery_reports_confirmed_post**
> delivery_reports_confirmed_post(delivery_report_id, account=account)

Confirm the receipt of delivery reports.

The confirm delivery reports endpoint will update the specified delivery reports as confirmed, confirmed delivery reports will no longer be returned in check delivery reports requests.

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
api_instance = swagger_client.DeliveryReportsApi()
delivery_report_id = swagger_client.DeliveryReportId() # DeliveryReportId | A list of delivery report IDs to mark as confirmed.
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # Confirm the receipt of delivery reports.
    api_instance.delivery_reports_confirmed_post(delivery_report_id, account=account)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->delivery_reports_confirmed_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_report_id** | [**DeliveryReportId**](DeliveryReportId.md)| A list of delivery report IDs to mark as confirmed. | 
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

void (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delivery_reports_get**
> DeliveryReports delivery_reports_get(account=account)

This endpoint is used to check for unconfirmed reports.

The reports endpoint returns the first 100 delivery reports that have been received and haven't been confirmed using the confirm reports endpoint.

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
api_instance = swagger_client.DeliveryReportsApi()
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try: 
    # This endpoint is used to check for unconfirmed reports.
    api_response = api_instance.delivery_reports_get(account=account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->delivery_reports_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. | [optional] 

### Return type

[**DeliveryReports**](DeliveryReports.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

