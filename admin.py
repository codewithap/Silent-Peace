from flask import Blueprint, render_template


# Defining a blueprint
admin = Blueprint(
    'admin', __name__,
    template_folder='adminTemplates',
    static_folder='adminStatic'
)

@admin.route('/')   # Focus here
def admin_home():
    return render_template("admin.html")

