from pydantic import BaseModel


class IdentityVerification(BaseModel):
    idType: str
    stateOfIssue: str
    licenseNumber: str
    acceptLicenseTerm: bool | None = True
    firstName: str
    familyName: str
    dobDay: str
    dobMonth: str
    dobYear: str
    middleName: str | None = None
    noMiddleName: bool
