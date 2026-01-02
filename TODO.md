# TODO: Fix Codebase Issues

- [x] Update requirements.txt to include PyJWT dependency
- [x] Fix utils/validator.py to raise ValidationError instead of strings
- [x] Fix utils/token.py import for ValidationError
- [x] Fix services/auth_service.py to return dict from login_user
- [x] Remove unnecessary print from database/fake_db.py
- [x] Remove redundant /login route and debug print from app.py
- [x] Update middlewares/auth_middleware.py to use flask.g for user data
- [x] Update routes/auth.py to use g.user instead of request.user
- [x] Fix deprecated datetime.utcnow() in utils/token.py
