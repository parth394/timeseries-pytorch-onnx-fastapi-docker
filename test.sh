curl -X 'POST' \
  'http://localhost:80/predict' \
  -H 'accept: application/json' \
  -H 'token: 1337' \
  -H 'Content-Type: application/json' \
  -d '{
  "sequence": [59, 78, 67, 89, 100]
}'