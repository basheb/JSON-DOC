# generated by datamodel-codegen:
#   filename:  example.json
#   timestamp: 2024-09-10T15:45:21+00:00

from __future__ import annotations

from typing import Optional

from jsondoc.models.block.types.rich_text.base import RichTextBase
from jsondoc.models.shared_definitions import Annotations
from pydantic import BaseModel, ConfigDict
from typing_extensions import Literal


class Link(BaseModel):
    url: str


class Text(BaseModel):
    content: str
    link: Optional[Link] = None


class RichTextText(RichTextBase):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    type: Literal['text'] = 'text'
    text: Text
    annotations: Annotations
    plain_text: str
    href: Optional[str] = None
