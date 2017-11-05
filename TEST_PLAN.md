Pyramid Test Thought Process
========================

Home Route
---------------
- Test if the data base gets initiated
    - Table gets created
    - Journals can be access

Detail Route
- Test if detail route returns the correct journal per request id


Edit Route
- Test if the GET works correct entry is pulled to be edited
- Test if the POST works: the data base query is successful
- Test if 404 is being passed back with request id that doesn't exist

Create Route
- Test if the new journal gets created by asserting it in the detail view
- Test if 404 is being passed back with empty or invalid request