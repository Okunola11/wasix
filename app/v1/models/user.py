from sqlalchemy import Column, String, ForeignKey, Boolean, text, DateTime
from sqlalchemy.orm import relationship, mapped_column
from .base_model import BaseTableModel

class User(BaseTableModel):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_admin = Column(Boolean, server_default=text("false"))
    is_active = Column(Boolean, server_default=text("false"))
    is_deleted = Column(Boolean, server_default=text("false"))
    verified_at = Column(DateTime(timezone=True), nullable=True, default=None)

    oauth = relationship("OAuth", uselist=False, back_populates="user", cascade="all, delete-orphan")
    tokens = relationship("UserToken", back_populates="user")

    def to_dict(self):
        obj_dict = super().to_dict()
        obj_dict.pop("password")
        return obj_dict

    def get_context_string(self, context: str):
        """
        Generates a unique context string for a user
        """
        return f"{context}{self.password[-6:]}{self.updated_at.strftime('%m%d%Y%H%M%S')}".strip()

    def __str__(self):
        return self.email
