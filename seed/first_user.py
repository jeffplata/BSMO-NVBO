from auth.models import User, Role
from extensions import db
from flask_security.utils import hash_password

admin_role = Role(name="admin", description="Administrator")
db.session.add(admin_role)
db.session.commit()

admin_user = User(email="admin@example.com", password=hash_password("password123"), roles=[admin_role])
db.session.add(admin_user)
db.session.commit()
