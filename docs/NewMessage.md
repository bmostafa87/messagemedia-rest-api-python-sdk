# NewMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Content of message. | 
**callback_url** | **str** | URL replies and delivery reports to this message will be pushed to. | [optional] 
**delivery_report** | **bool** |  | [optional] [default to False]
**destination_number** | **str** | Destination number of the message. | 
**format** | **str** | Format of message. | [optional] [default to 'SMS']
**metadata** | [**MessageMetadata**](MessageMetadata.md) |  | [optional] 
**message_expiry_timestamp** | **datetime** | Date time after which the message is considered expired in ISO8601 format. | [optional] 
**scheduled** | **datetime** | Date time at which the message is scheduled for in ISO8601 format. | [optional] 
**source_address** | **str** |  | [optional] 
**source_address_type** | **str** | Type of source address specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


