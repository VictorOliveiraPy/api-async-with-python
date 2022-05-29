import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def post(self):
        raise NotImplemented
    