import json

import grequests

from app.schemas import IdentityVerification


def identity_verification(data: IdentityVerification = None):
    req_data = {
        "data": {
            "idType": data.idType,
            "stateOfIssue": data.stateOfIssue,
            "licenseNumber": data.licenseNumber,
            "acceptLicenseTerm": True,
            "firstName": data.firstName,
            "familyName": data.familyName,
            "dobDay": data.dobDay,
            "dobMonth": data.dobMonth,
            "dobYear": data.dobYear,
            "noMiddleName": True
        }
    }
    if not data.noMiddleName:
        req_data["data"]["noMiddleName"] = False
        req_data["data"]["middleName"] = data.middleName
    return req_data


def req_identity_verification(data: list):
    req_list = [grequests.post(url="https://tapi.telstra.com/prepaid/activation/bff/customers/document", headers={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "225",
        "Content-Type": "application/json",
        "Host": "tapi.telstra.com",
        "Origin": "https://prepaid.activate.boost.com.au",
        "Pragma": "no-cache",
        "Referer": "https://prepaid.activate.boost.com.au/",
        "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-request-application": "BPPA"
    }, data=json.dumps(i)) for i in data]
    res_list = grequests.map(req_list)
    try:
        res_status = [json.loads(i.content)["status"] for i in res_list]
    except Exception as reqs:
        print(res_list)
    return res_status
