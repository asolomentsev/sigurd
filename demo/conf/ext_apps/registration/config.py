import sigurd

class Settings(sigurd.AppConfig):
    ACCOUNT_ACTIVATION_DAYS = 7

    def install(self):
        self.install_app("registration")

    def get_urls(self):
        self.install_urls(r'^accounts/', 'registration.backends.default.urls')