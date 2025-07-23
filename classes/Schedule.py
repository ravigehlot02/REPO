from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import List, Optional, Literal

class Schedule(BaseModel):
    time:datetime
    image_url:Optional[HttpUrl] = None
    caption:Optional[str] = Field(default="",max_length=2200)
    posted:bool= False
    platform:List[Literal["instagram","facebook","x","linkedin","youtube"]]
    media_type:str