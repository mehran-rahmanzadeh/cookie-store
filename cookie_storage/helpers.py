from collections.abc import Iterator

from django.conf import settings


def validate_session_serializer(func):
    """check session serializer is compatible with helper class"""
    def inner(*args, **kwargs):
        if settings.SESSION_SERIALIZER != SessionHelper.session_serializer:
            raise Exception(f'SESSION_SERIALIZER should be {SessionHelper.session_serializer}')
        return func(*args, **kwargs)
    return inner


class SessionHelper:
    """Manipulates data in Session"""
    session_serializer = 'django.contrib.sessions.serializers.PickleSerializer'

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(SessionHelper, self).__init__(*args, **kwargs)

    @staticmethod
    def __get_obj_key(klass):
        return f'{klass.__module__}.{klass.__name__}'

    @validate_session_serializer
    def set(self, obj):
        """set data to session"""
        if isinstance(obj, Iterator):
            obj = list(obj)
            if not obj:
                return
            key = self.__get_obj_key(obj[0].__class__)
        else:
            key = self.__get_obj_key(obj.__class__)
        self.request.session[key] = obj
        self.request.session.modified = True

    @validate_session_serializer
    def get(self, klass):
        """get data from session"""
        return self.request.session.get(self.__get_obj_key(klass))

    def delete(self, klass):
        """delete data from session"""
        del self.request.session[self.__get_obj_key(klass)]
        self.request.session.modified = True

    def clear(self):
        """clear session"""
        self.request.session.flush()
        self.request.session.modified = True
