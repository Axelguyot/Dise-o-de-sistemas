class RouteApp:
    def init_app(self, app):
        from app.resources import user_bp, home_bp
        app.register_blueprint(user_bp, url_prefix='/api/v1')
        app.register_blueprint(home_bp, url_prefix='/api/v1')
        pass