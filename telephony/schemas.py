
from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class CdrSviBase(BaseModel):
    id: int
    ref: str
    ref_id: int
    contact_id: int
    num_compose: str
    src: str
    dst: str
    duration: int
    billsec: int
    start: datetime
    answer: datetime
    end: datetime
    calltype: int
    disposition: str
    clid: str
    dcontext: str
    channel: str
    # dstchannel: str
    uniqueid: str
    # userfield: str
    amaflags: str

# class CdrSviCreate(CdrSviBase):
#     pass


class CdrSvi(CdrSviBase):
    id: int
    ref: str
    ref_id: int
    contact_id: int
    num_compose: str


    class Config:
        orm_mode = True


class CdrOutBase(BaseModel):
    id: int
    src: str
    dst: str

# class CdrSviCreate(CdrSviBase):
#     pass


class CdrOut(CdrOutBase):
    id: int
    src: str
    dst: str

    class Config:
        orm_mode = True
