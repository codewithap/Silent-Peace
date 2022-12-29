from flask import Blueprint


# Defining a blueprint
admin = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static'
)

@admin.route('/admin')   # Focus here
def admin_home():
    return "Hello Admin!" 