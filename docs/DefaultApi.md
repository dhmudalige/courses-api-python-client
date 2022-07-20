# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_course_by_code**](DefaultApi.md#get_course_by_code) | **GET** /{semester}/{courseCode}/ | 
[**get_course_details_by_semester**](DefaultApi.md#get_course_details_by_semester) | **GET** /{semester}/ | 
[**get_courses**](DefaultApi.md#get_courses) | **GET** / | 


# **get_course_by_code**
> Course get_course_by_code(semester, course_code)



Returns the details of the specified course

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
semester = 'semester_example' # str | Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)
course_code = 'course_code_example' # str | Course Code

try:
    api_response = api_instance.get_course_by_code(semester, course_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_course_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semester** | **str**| Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester) | 
 **course_code** | **str**| Course Code | 

### Return type

[**Course**](Course.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_details_by_semester**
> CourseList get_course_details_by_semester(semester)



Retuns the list of available courses the specified semester

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
semester = 'semester_example' # str | Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)

try:
    api_response = api_instance.get_course_details_by_semester(semester)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_course_details_by_semester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semester** | **str**| Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester) | 

### Return type

[**CourseList**](CourseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courses**
> CourseList get_courses()



Retuns the list of all available courses

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_courses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_courses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CourseList**](CourseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

