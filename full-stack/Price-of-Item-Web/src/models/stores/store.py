import uuid
from src.common.database import Database
import src.models.stores.constants as StoreConstants
import src.models.stores.errors as StoreErrors


class Store(object):
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {"name": self.name,
                "url_prefix": self.url_prefix,
                "tag_name": self.tag_name,
                "query": self.query,
                "_id": self._id}

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(collection=StoreConstants.COLLECTION,
                                       query={"_id": id}))

    @classmethod
    def get_by_name(cls, store_name):
        return cls(**Database.find_one(collection=StoreConstants.COLLECTION,
                                       query={"name": store_name}
                                       ))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        return cls(**Database.find_one(collection=StoreConstants.COLLECTION,
                                      query={"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        for i in range(0, len(url)):
            try:
                store = cls.get_by_url_prefix(url[:1])
                return store
            except:
                raise StoreErrors.StoreNotFoundException("The URL prefix used to find the store came back empty")

    def save_to_db(self):
        Database.insert(collection=StoreConstants.COLLECTION,
                        data=self.json())