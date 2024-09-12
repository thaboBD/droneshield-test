# API Test Bug report

1. Create endpoint allows for empty body to be sent
Priority: medium
Severity: low
expected result: a 400 bad request error. api endpoint needs better validation
curl to reproduce issue
```
curl -X 'POST' \
  'https://petstore.swagger.io/v2/pet' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{}'
```




# UI Test Bug report
1. User is able to checkout with an empty cart
priority: medium
serverity: medium
Steps to reproduce
- login to the app
- click on the cart icon on the top right
-  click checkout and enter user details
- click continue then finish
Expected result: the user should bit be abke to click checkout if the cart is empty
Actual result: the user is able to complete the checkout flow  with an empty cart

