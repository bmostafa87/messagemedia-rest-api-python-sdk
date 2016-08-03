# swagger_client
Australia’s Leading Messaging Solutions for Business and Enterprise.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build date: 2016-08-03T00:31:44.783Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.DeliveryReportsApi
delivery_report_id = swagger_client.DeliveryReportId() # DeliveryReportId | A list of delivery report IDs to mark as confirmed.
account = 'account_example' # str | The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts. (optional)

try:
    # Confirm the receipt of delivery reports.
    api_instance.delivery_reports_confirmed_post(delivery_report_id, account=account)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->delivery_reports_confirmed_post: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.messagemedia.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeliveryReportsApi* | [**delivery_reports_confirmed_post**](docs/DeliveryReportsApi.md#delivery_reports_confirmed_post) | **POST** /delivery_reports/confirmed | Confirm the receipt of delivery reports.
*DeliveryReportsApi* | [**delivery_reports_get**](docs/DeliveryReportsApi.md#delivery_reports_get) | **GET** /delivery_reports | This endpoint is used to check for unconfirmed reports.
*MessagingApi* | [**messages_message_id_get**](docs/MessagingApi.md#messages_message_id_get) | **GET** /messages/{messageId} | Retrive the status and details of a submitted message.
*MessagingApi* | [**messages_message_id_put**](docs/MessagingApi.md#messages_message_id_put) | **PUT** /messages/{messageId} | Update the status of a submitted message.
*MessagingApi* | [**messages_post**](docs/MessagingApi.md#messages_post) | **POST** /messages | Send one or more SMS or text to voice messages.
*RepliesApi* | [**replies_confirmed_post**](docs/RepliesApi.md#replies_confirmed_post) | **POST** /replies/confirmed | Confirm the receipt of replies.
*RepliesApi* | [**replies_get**](docs/RepliesApi.md#replies_get) | **GET** /replies | Check for unconfirmed replies.


## Documentation For Models

 - [DeliveryReport](docs/DeliveryReport.md)
 - [DeliveryReportId](docs/DeliveryReportId.md)
 - [DeliveryReports](docs/DeliveryReports.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [Message](docs/Message.md)
 - [MessageList](docs/MessageList.md)
 - [MessageMetadata](docs/MessageMetadata.md)
 - [Messages](docs/Messages.md)
 - [NewMessage](docs/NewMessage.md)
 - [Replies](docs/Replies.md)
 - [Reply](docs/Reply.md)
 - [ReplyId](docs/ReplyId.md)
 - [Status](docs/Status.md)


## Documentation For Authorization


## hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



