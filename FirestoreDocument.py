from abc import ABC, abstractclassmethod
from threading import Event
from .utils import generate_reference
from .setup import database


class FirestoreDocument(ABC):
