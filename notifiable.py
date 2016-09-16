class Notifiable(object):
    def notify(self, e):
        e_handle = 'handle_%s' % e.__class__.__name__
        if hasattr(self, e_handle) and hasattr(getattr(self, e_handle), '__call__'):
            getattr(self, e_handle)(e)
