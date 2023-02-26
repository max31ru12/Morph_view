class MainPageMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = [
            {'block': 'Главная'},
            {'block': 'О нас'},
            {'block': 'Пациентам'},
            {'block': 'Врачам'},
            {'block': 'Литература'},
        ]
        return context




