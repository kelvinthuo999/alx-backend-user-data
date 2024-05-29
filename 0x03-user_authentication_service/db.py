#!/usr/bin/env python3

"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        :param email: The email of the user.
        :param hashed_password: The hashed password of the user.
        :return: The newly created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.

        :param kwargs: Arbitrary keyword arguments to filter the query.
        :return: The first User object that matches the query.
        :raises NoResultFound: If no user is found.
        :raises InvalidRequestError: If the query is invalid.
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the specified attributes")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query parameters")

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes.

        :param user_id: The ID of the user to update.
        :param kwargs: Arbitrary keyword arguments to update the user's attributes.
        :raises ValueError: If an attribute that does not correspond to a User attribute is passed.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Attribute {key} does not exist on User")
            setattr(user, key, value)
        self._session.commit()
