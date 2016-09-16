import uuid


class UID(object):
    def __init__(self, uid=None):
        if uid:
            self.uid = uid
        else:
            self.uid = uuid.uuid4()
