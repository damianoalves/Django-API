

def check_create_permission(user, obj):
    return user.has_perm('add_' + obj.__class__.__name__.lower(), obj)


def check_read_permission(user, obj):
    return user.has_perm('view_' + obj.__class__.__name__.lower(), obj)


def check_update_permission(user, obj):
    return user.has_perm('change_' + obj.__class__.__name__.lower(), obj)


def check_delete_permission(user, obj):
    return user.has_perm('delete_' + obj.__class__.__name__.lower(), obj)
