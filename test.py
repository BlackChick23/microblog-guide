import requests

url = "https://api-man1.kiotviet.vn/api/ordersuppliers"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IndYYSJ9.eyJpc3MiOiJrdnNzand0Iiwic3ViIjoxMDAwNTM1MzUxLCJpYXQiOjE3NDU1MDI1MTYsImV4cCI6MTc0NzkyMTcxNiwicHJlZmVycmVkX3VzZXJuYW1lIjoiVEdTRjY0NSIsInJvbGVzIjpbIlVzZXIiXSwicGVybXMiOiIiLCJrdnNvdXJjZSI6IlJldGFpbCIsImt2dXNldGZhIjowLCJrdndhaXRvdHAiOjAsImt2c2VzIjoiZDljODBkZTlhM2ZhNDg0ODkwMjkyYjY0Y2IzNTZjZDgiLCJrdnVpZCI6MTAwMDUzNTM1MSwia3ZsYW5nIjoidmktVk4iLCJrdnV0eXBlIjowLCJrdnVsaW1pdCI6IkZhbHNlIiwia3Z1YWRtaW4iOiJGYWxzZSIsImt2dWFjdCI6IlRydWUiLCJrdnVsaW1pdHRyYW5zIjoiRmFsc2UiLCJrdnVzaG93c3VtIjoiVHJ1ZSIsImt2YmkiOiJUcnVlIiwia3ZjdHlwZSI6MiwidXNlQkkiOnsiQ3VzdG9tZXJCSVJlcG9ydF9SZWFkIjpbXSwiU2FsZUJJUmVwb3J0X1JlYWQiOltdLCJQcm9kdWN0QklSZXBvcnRfUmVhZCI6W10sIkZpbmFuY2VCSVJlcG9ydF9SZWFkIjpbXX0sImt2YmlkIjo4NTk5NSwia3ZyaW5kaWQiOjIsImt2cmNvZGUiOiJ0Z3NmIiwia3ZyaWQiOjM2NjU0MCwia3Z1cmlkIjozNjY1NDAsImt2cmdpZCI6Mn0.DapkpmffRfj3LH5IngPzr8xMgy3MexEudHVOf3wFAYrQzPV4zW8DNAqFFpPl_aTleq7mgxhrxmiLtqtPGIDc3JK_XxKJk3Nr3OuuMih1o7PMplxneAdFYnPHpKh6BZgAYCspaQfSTSaX501gZzOdg4yfrhVhNNqayZg7f0utxts1QppqC1XpK5aPbnkyJImCYCdZYl6q13BRo3xLJ6wxhpBgXHHNlHEt8xCqZ0cpP5KkZd4Z2nvVk-k4wFOtdMClVX04QM-y3Atn-_kkUJbIyvgeb38rn_NNK7a96cV2deX_0ROLVTS_28M-lVjGf0FPeTSj_KUnOCu7DeaYFfCaxg",
    "BranchId": "85995",
    "Connection": "keep-alive",
    "FingerPrintKey": "16a470a6d55180670bb4a5ae869739fc_Safari_Desktop_Máy tính Mac OS",
    "Host": "api-man1.kiotviet.vn",
    "IsUseKvClient": "1",
    "Origin": "https://tgsf.kiotviet.vn",
    "Referer": "https://tgsf.kiotviet.vn/",
    "Retailer": "tgsf",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "X-GROUP-ID": "2",
    "X-Language": "vi-VN",
    "X-RETAILER-CODE": "tgsf"
}

params = {
    "format": "json",
    "Includes": [
        "Branch", "Total", "PaidAmount", "TotalQuantity",
        "TotalProductType", "SubTotal", "Supplier",
        "User", "User1", "PurchaseOrders"
    ],
    "ForSummaryRow": "true",
    "$inlinecount": "allpages",
    "BranchIds": "[85995]",
    "OrderStatus": '["0","1","2","3"]',
    "$top": 15,
    "$filter": "OrderDate eq 'month'"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
