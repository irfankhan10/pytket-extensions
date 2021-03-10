# Copyright 2021 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, ClassVar, Dict, Optional, Type
from dataclasses import dataclass
from pytket.config import PytketExtConfig


@dataclass
class QSharpConfig(PytketExtConfig):
    ext_dict_key: ClassVar[str] = "qsharp"

    resourceId: Optional[str]
    location: Optional[str]
    storage: Optional[str]

    @classmethod
    def from_extension_dict(
        cls: Type["QSharpConfig"], ext_dict: Dict[str, Any]
    ) -> "QSharpConfig":
        return cls(
            ext_dict.get("resourceId", None),
            ext_dict.get("location", None),
            ext_dict.get("storage", None),
        )
