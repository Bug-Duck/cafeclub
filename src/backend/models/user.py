import re
import typing
class User:
    def __init__(self) -> None:
        self.id: typing.Optional[int]
        self.registered_on: int
        self.username: str
        self.email: str
        self.password: str
        self.tags: list[str]
        self.avatar: typing.Optional[str]
        self.bio: typing.Optional[str]
    def _from_sql(self,sql: tuple) -> 'User':
        self.id = sql[0]
        self.registered_on = sql[1]
        self.username = sql[2]
        self.email = sql[3]
        self.password = sql[4]
        self.tags = sql[5].split(",")
        self.avatar = sql[6]
        self.bio = sql[7]
        return self
    def _to_sql(self, specify_id=False) -> None:
        if specify_id:
            return (self.id, self.registered_on, self.username, self.email, self.password, ','.join(self.tags), self.avatar, self.bio)
        else:
            return (self.registered_on, self.username, self.email, self.password, ','.join(self.tags), self.avatar, self.bio)
    def validate(self) -> tuple[bool, str]:
        if len(self.username) < 3 or len(self.username) > 20:
            return (False, "Username length must be between 3 and 20 characters")
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email) == None:
            return (False, "Invalid email")
        if len(self.password) != 512:
            return (False, "Invalid password")
        if self.bio and len(self.bio) > 100:
            return (False, "Bio length must be less than 100 characters")
        if self.avatar and re.match(r"https?://\S+", self.avatar) == None:
            return (False, "Invalid avatar")
        return (True, "Valid")