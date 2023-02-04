from fastapi import FastAPI
from pydantic import BaseModel

import http.client
import json

class Item(BaseModel):
    url:str


app = FastAPI()

@app.get("/")
def hello():

  conn = http.client.HTTPSConnection("eapi.stalcraft.net")

  headersList = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxNDIiLCJqdGkiOiI4MDExMzIxODUyMjk5OWYxZTFlN2Q3NmJlNDU1MzJjN2I5Y2M1YzRmZTQ5MjBjMTlkNTIzNDg3ZGQzYmVhMjA2NTg1ZTUyYTk5YmU1NTE2OSIsImlhdCI6MTY3NTQ0ODA1OS4wNjQ0NSwibmJmIjoxNjc1NDQ4MDU5LjA2NDQ1MiwiZXhwIjoxNzA2OTg0MDU4LjQ4MDYxNCwic3ViIjoiMjUzMjE1NSIsInNjb3BlcyI6W119.nx-sV6YtwJ8KUDtTLPkPkTxO9eRkwyBIAPCHPBkMPmNkoQ5J-0w7Qutcuaucv-qEgkrlbjytPYRFLG4pasJPETeRc5G94oeEXiOgVspzJKVLz2jlH_qd2_iAsmq7zP09ZdYt49MGkqVGHitExYN-Fyhqo8a9IbjCpO6rPjTgXYbnUx3uuDmE8oM-Pf6nuIiyc7z8BC4ITw-CckxFSPMbxamOdUmUPAjw9oBMGzmx8ac1WUNqJ3Wuds3Pg53TMfvExoD3jvfYl2wQL4zMDzTDcP_AZsnmFn7ATORCP5Jkcdmfmbv2WZCmbdiajiEE7bCVScDWpLTIQ-2Dy7YGsZ6RAcS_6XvPpPZALuN-R05qq8OajwmPArPX2JoW97oc6kMHwLD1Jk0jrN3vEBDIMeHu2UL5yxyc3eO3CXDz2EMEnS8WWO_3QQfSL_eMVgm0ZzswlJE5mKvGgqhzq9HjuUWh6cZYyfR5yL7MUxlZ0jthlj8d7vsveoXGJQOJvCyl3ylFb4o1yDdxNH38fSBOx2ULShOjGsUCZeOzDRC569y0qUunJSlFeySoYoaitAQfQTIVJc3miUkaaNN9eASMRbxFCny7fKxvNHf95CzAKURcrFsWbdtG6gLAXtCpL_Xo2PNTlP-cdOUyeWmI-cFAR54RuiJO0lz69Z-oTdIk0ZnXie0"}

  payload = ""

  conn.request("GET", "/characters/NA/name/JCzar", payload, headersList)
  response = conn.getresponse()
  result = response.read()

  print(result.decode("utf-8"))
  return json.loads(result)



@app.post("/porBody/")
def hello(item:Item):


  conn = http.client.HTTPSConnection("eapi.stalcraft.net")

  headersList = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxNDIiLCJqdGkiOiI4MDExMzIxODUyMjk5OWYxZTFlN2Q3NmJlNDU1MzJjN2I5Y2M1YzRmZTQ5MjBjMTlkNTIzNDg3ZGQzYmVhMjA2NTg1ZTUyYTk5YmU1NTE2OSIsImlhdCI6MTY3NTQ0ODA1OS4wNjQ0NSwibmJmIjoxNjc1NDQ4MDU5LjA2NDQ1MiwiZXhwIjoxNzA2OTg0MDU4LjQ4MDYxNCwic3ViIjoiMjUzMjE1NSIsInNjb3BlcyI6W119.nx-sV6YtwJ8KUDtTLPkPkTxO9eRkwyBIAPCHPBkMPmNkoQ5J-0w7Qutcuaucv-qEgkrlbjytPYRFLG4pasJPETeRc5G94oeEXiOgVspzJKVLz2jlH_qd2_iAsmq7zP09ZdYt49MGkqVGHitExYN-Fyhqo8a9IbjCpO6rPjTgXYbnUx3uuDmE8oM-Pf6nuIiyc7z8BC4ITw-CckxFSPMbxamOdUmUPAjw9oBMGzmx8ac1WUNqJ3Wuds3Pg53TMfvExoD3jvfYl2wQL4zMDzTDcP_AZsnmFn7ATORCP5Jkcdmfmbv2WZCmbdiajiEE7bCVScDWpLTIQ-2Dy7YGsZ6RAcS_6XvPpPZALuN-R05qq8OajwmPArPX2JoW97oc6kMHwLD1Jk0jrN3vEBDIMeHu2UL5yxyc3eO3CXDz2EMEnS8WWO_3QQfSL_eMVgm0ZzswlJE5mKvGgqhzq9HjuUWh6cZYyfR5yL7MUxlZ0jthlj8d7vsveoXGJQOJvCyl3ylFb4o1yDdxNH38fSBOx2ULShOjGsUCZeOzDRC569y0qUunJSlFeySoYoaitAQfQTIVJc3miUkaaNN9eASMRbxFCny7fKxvNHf95CzAKURcrFsWbdtG6gLAXtCpL_Xo2PNTlP-cdOUyeWmI-cFAR54RuiJO0lz69Z-oTdIk0ZnXie0"
  }
  

  payload = ""

  conn.request("GET", item.url, payload, headersList)
  response = conn.getresponse()
  result = response.read()

  print(result.decode("utf-8"))
  return json.loads(result)


@app.post("/porParam/")
def hello(datourl:str):
 
  
  conn = http.client.HTTPSConnection("eapi.stalcraft.net")

  headersList = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxNDIiLCJqdGkiOiI4MDExMzIxODUyMjk5OWYxZTFlN2Q3NmJlNDU1MzJjN2I5Y2M1YzRmZTQ5MjBjMTlkNTIzNDg3ZGQzYmVhMjA2NTg1ZTUyYTk5YmU1NTE2OSIsImlhdCI6MTY3NTQ0ODA1OS4wNjQ0NSwibmJmIjoxNjc1NDQ4MDU5LjA2NDQ1MiwiZXhwIjoxNzA2OTg0MDU4LjQ4MDYxNCwic3ViIjoiMjUzMjE1NSIsInNjb3BlcyI6W119.nx-sV6YtwJ8KUDtTLPkPkTxO9eRkwyBIAPCHPBkMPmNkoQ5J-0w7Qutcuaucv-qEgkrlbjytPYRFLG4pasJPETeRc5G94oeEXiOgVspzJKVLz2jlH_qd2_iAsmq7zP09ZdYt49MGkqVGHitExYN-Fyhqo8a9IbjCpO6rPjTgXYbnUx3uuDmE8oM-Pf6nuIiyc7z8BC4ITw-CckxFSPMbxamOdUmUPAjw9oBMGzmx8ac1WUNqJ3Wuds3Pg53TMfvExoD3jvfYl2wQL4zMDzTDcP_AZsnmFn7ATORCP5Jkcdmfmbv2WZCmbdiajiEE7bCVScDWpLTIQ-2Dy7YGsZ6RAcS_6XvPpPZALuN-R05qq8OajwmPArPX2JoW97oc6kMHwLD1Jk0jrN3vEBDIMeHu2UL5yxyc3eO3CXDz2EMEnS8WWO_3QQfSL_eMVgm0ZzswlJE5mKvGgqhzq9HjuUWh6cZYyfR5yL7MUxlZ0jthlj8d7vsveoXGJQOJvCyl3ylFb4o1yDdxNH38fSBOx2ULShOjGsUCZeOzDRC569y0qUunJSlFeySoYoaitAQfQTIVJc3miUkaaNN9eASMRbxFCny7fKxvNHf95CzAKURcrFsWbdtG6gLAXtCpL_Xo2PNTlP-cdOUyeWmI-cFAR54RuiJO0lz69Z-oTdIk0ZnXie0"
  }

  payload = ""

  conn.request("GET", datourl, payload, headersList)
  response = conn.getresponse()
  result = response.read()

  print(result.decode("utf-8"))
  return json.loads(result)