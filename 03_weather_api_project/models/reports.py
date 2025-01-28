import datetime
from typing import Optional
from pydantic import BaseModel
from models.location import Location
import uuid


class ReportSubmittal(BaseModel):
    description: str
    location: Location


class Report(ReportSubmittal):
    id: str
    created_date: Optional[datetime.datetime]
