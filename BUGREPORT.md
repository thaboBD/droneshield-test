API Test Bug reports

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