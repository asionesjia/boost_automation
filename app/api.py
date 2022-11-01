import io
import os
import uuid

import openpyxl
from fastapi import UploadFile, APIRouter, HTTPException
from starlette import status
from starlette.background import BackgroundTask
from starlette.responses import FileResponse

from app.main import identity_verification, req_identity_verification
from app.schemas import IdentityVerification

application = APIRouter()


@application.post("/uploadFile/")
async def create_upload_file(file: UploadFile):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        xlsx = io.BytesIO(f)
        wb = openpyxl.load_workbook(xlsx)
        ws = wb.active
        rows = ws.iter_rows()
        data = []
        req_data = []
        for cells in rows:
            row = []
            for cell in cells:
                row.append(cell.value)
            data.append(row)
        for item in data:
            if not data.index(item):
                ws['I1'].value = "IdentityVerification"
                continue
            if not item[5]:
                mn = True
            else:
                mn = False
            date = item[7].split("/")
            req_data.append(identity_verification(IdentityVerification(
                idType=item[1],
                stateOfIssue=item[2],
                licenseNumber=item[3],
                firstName=item[4],
                middleName=item[5],
                familyName=item[6],
                noMiddleName=mn,
                dobDay=date[0],
                dobMonth=date[1],
                dobYear=date[2]
            )))
        res_status = req_identity_verification(req_data)
        for item in data:
            if not data.index(item):
                ws['I1'].value = "IdentityVerification"
                continue
            ws[f'I{data.index(item) + 1}'].value = res_status[data.index(item) - 1]
        filename = f'{uuid.uuid4()}.xlsx'
        wb.save(filename)
        wb.close()
        return FileResponse(
            filename,
            filename=filename,
            background=BackgroundTask(lambda: os.remove(filename)),
        )
    else:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

