from enum import Enum

from pydantic import IPvAnyAddress, field_serializer

from src.schema import YAMLSchema


class ServerRole(str, Enum):
    """Server roles enumeration for YAML schema."""

    WEB = "web"
    PROXY = "proxy"
    DATABASE = "database"


class ServerSchema(YAMLSchema):
    """YAML Server schema."""

    name: str
    ip: IPvAnyAddress
    roles: list[ServerRole]
    config: dict[str, str | int] | None = None

    @field_serializer("ip")
    def serialize_ip(self, ip: IPvAnyAddress, _info) -> str:
        """Serialize IP address to string on serialization.

        Args:
            ip (IPvAnyAddress): IP address.
            _info: Field information.

        Returns:
            str: IP address as string.

        """

        return str(ip)
