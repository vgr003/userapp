class User:
    route_app_labels = {'user'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db =='user'
        return None

class Product:
    route_app_labels = {'product'}
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db =='product'
        return None