from sqlalchemy.orm import Mapped

from .base import Base


class Product(Base):
    '''
    Здесь должны были явно указать __tablename__ = "название", но мы создали декорированную функцию
    в файле base.py, который берет имя класса, переводит его в нижний регистр и добавляет в конце букву s  
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    '''

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]