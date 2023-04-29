from django.apps import AppConfig


class VacancyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vacancy'

    def ready(self):
        from vacancy.signal_handlers import connect_signal_handlers

        connect_signal_handlers()
