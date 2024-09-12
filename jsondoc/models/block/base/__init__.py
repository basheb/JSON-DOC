# generated by datamodel-codegen:
#   filename:  example.json
#   timestamp: 2024-09-10T15:45:21+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import AwareDatetime, BaseModel, ConfigDict
from typing_extensions import Literal


class Parent(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: str
    block_id: Optional[str] = None
    page_id: Optional[str] = None


class CreatedBy(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    object: Literal['user']
    id: str


class LastEditedBy(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    object: Literal['user']
    id: str


class BlockBase(BaseModel):
    object: Literal['block'] = 'block'
    id: str
    parent: Optional[Parent] = None
    type: str
    created_time: AwareDatetime
    created_by: Optional[CreatedBy] = None
    last_edited_time: Optional[AwareDatetime] = None
    last_edited_by: Optional[LastEditedBy] = None
    archived: Optional[bool] = None
    in_trash: Optional[bool] = None
    has_children: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None
