from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
# api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(swagger_client.Configuration()))
# api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration=swagger_client.Configuration(host='https://localhost')))
semester = 'semester_example' # str | Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)
course_code = 'course_code_example' # str | Course Code

try:
    api_response = api_instance.get_course_by_code(semester, course_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_course_by_code: %s\n" % e)